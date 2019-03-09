import pandas as pd

df = pd.read_csv('0020935-181108115102211.csv', sep=';', error_bad_lines=False)

dropCols = ['gbifID', 'datasetKey', 'occurrenceID', 'kingdom', 'phylum', 'class', 'order', 'family', 'genus',
            'infraspecificEpithet', 'taxonRank', 'countryCode', 'publishingOrgKey', 'species', 'taxonKey', 'speciesKey',
            'institutionCode', 'catalogNumber', 'license', 'mediaType', 'issue']

for i in dropCols:
    df = df.drop(i, axis=1)

to_maxent = df.filter(['scientificName', 'decimalLatitude', 'decimalLongitude'], axis=1)

to_maxent = to_maxent.replace('Myotis nattereri (Kuhl, 1817)', 'M.nattereri')
to_maxent = to_maxent.replace('Myotis nattereri nattereri', 'M.nattereri')

to_maxent = to_maxent.rename(
    columns={'scientificName': 'SPECIES', 'decimalLatitude': 'LATITUDE', 'decimalLongitude': 'LONGITUDE'})

# to_maxent = to_maxent.drop_duplicates()

to_maxent['SPECIES'].unique()

# to_maxent.to_csv(path_or_buf='eu_nattereri.csv', sep=',', index=False, encoding='UTF-8')

# df.to_csv(path_or_buf='eu_updated.csv', sep=';', encoding='UTF-8')
