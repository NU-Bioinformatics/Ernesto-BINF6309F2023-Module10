import requests
import pandas as pd
import json
from collections import OrderedDict


apiUrl = 'https://www.ebi.ac.uk/gwas/rest/api'

variant = 'rs7329174'
requestUrl = '%s/singleNucleotidePolymorphisms/%s/associations?projection=associationBySnp' %(apiUrl, variant)
response = requests.get(requestUrl, headers={ "Content-Type" : "application/json"})

decoded = response.json()
#print(json.dumps(decoded, indent = 2))

for association in decoded['_embedded']['associations']:
    trait = ",".join([trait['trait'] for trait in association['efoTraits']])
    pvalue = association['pvalue']

    print("Trait: %s, p-value: %s" % (trait, pvalue))

# List of variants:
variants = ['rs142968358', 'rs62402518', 'rs12199222', 'rs7329174', 'rs9879858765']

# Store extracted data in this list:
extractedData = []

# Iterating over all variants:
for variant in variants:

    # Accessing data for a single variant:
    requestUrl = '%s/singleNucleotidePolymorphisms/%s/associations?projection=associationBySnp' % (apiUrl, variant)
    response = requests.get(requestUrl, headers={"Content-Type": "application/json"})

    # Testing if rsID exists:
    if not response.ok:
        print("[Warning] %s is not in the GWAS Catalog!!" % variant)
        continue

    # Test if the returned data looks good:
    try:
        decoded = response.json()
    except:
        print("[Warning] Failed to encode data for %s" % variant)
        continue

    for association in decoded['_embedded']['associations']:
        trait = ",".join([trait['trait'] for trait in association['efoTraits']])
        pvalue = association['pvalue']

        extractedData.append(OrderedDict({'variant': variant,
                                          'trait': trait,
                                          'pvalue': pvalue}))

# Format data into a table:
table = pd.DataFrame.from_dict(extractedData)
print(table)


def getStudy(studyLink):
    # Accessing data for a single study:
    response = requests.get(studyLink, headers={"Content-Type": "application/json"})
    decoded = response.json()

    accessionID = decoded['accessionId']
    pubmedId = decoded['publicationInfo']['pubmedId']

    return ((accessionID, pubmedId))


extractedData = []
for variant in variants:

    # Accessing data for a single variant:
    requestUrl = '%s/singleNucleotidePolymorphisms/%s/associations?projection=associationBySnp' % (apiUrl, variant)
    response = requests.get(requestUrl, headers={"Content-Type": "application/json"})

    # Testing if rsID exists:
    if not response.ok:
        print("[Warning] %s is not in the GWAS Catalog!!" % variant)
        continue

    # Test if the returned data looks good:
    try:
        decoded = response.json()
    except:
        print("[Warning] Failed to encode data for %s" % variant)
        continue

    for association in decoded['_embedded']['associations']:
        # extract study data:
        (accessionID, pubmedId) = getStudy(association['_links']['study']['href'])

        #
        trait = ",".join([trait['trait'] for trait in association['efoTraits']])
        pvalue = association['pvalue']

        extractedData.append(OrderedDict({'variant': variant,
                                          'trait': trait,
                                          'pvalue': pvalue,
                                          'accessionID': accessionID,
                                          'pubmedID': pubmedId
                                          }))

table = pd.DataFrame.from_dict(extractedData)
print(table)
table.to_excel('workshop.xlsx')