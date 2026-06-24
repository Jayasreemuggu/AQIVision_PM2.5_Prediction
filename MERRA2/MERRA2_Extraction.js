/*******************************************************
 AQIVision Project
 MERRA-2 Meteorological Data Extraction
 Google Earth Engine JavaScript

 Objective:
 Extract monthly meteorological parameters
 for all AQIVision cities from
 January 2015 to June 2020.

 Dataset:
 NASA/GSFC/MERRA/slv/2

 Output:
 AQIVision_MERRA2_2015_2020_Optimized.csv
********************************************************/


// ======================================================
// Load AQIVision City Locations
// ======================================================

// Replace this with your uploaded Earth Engine Asset

var cities = ee.FeatureCollection(
'projects/aqivision/assets/aqivision_cities'
);


// ======================================================
// Study Period
// ======================================================

var startDate = ee.Date('2015-01-01');
var endDate   = ee.Date('2020-07-01');

var totalMonths = endDate.difference(startDate,'month');

print("Total Months:", totalMonths);


// ======================================================
// Monthly Extraction
// ======================================================

var monthlyCollections = ee.List.sequence(
0,
totalMonths.subtract(1)
).map(function(m){

m = ee.Number(m);

var start = startDate.advance(m,'month');
var end   = start.advance(1,'month');


// Monthly Mean Image

var monthlyImage = ee.ImageCollection(
'NASA/GSFC/MERRA/slv/2'
)

.filterDate(start,end)

.mean()

.select([

'T2M',

'QV2M',

'PS',

'PBLTOP',

'U10M',

'V10M'

]);


// Extract values

var fc = monthlyImage.reduceRegions({

collection:cities,

reducer:ee.Reducer.mean(),

scale:50000

});


// Keep Required Fields

fc = fc.map(function(f){

return ee.Feature(null,{

City:f.get('City'),

Month:start.format('YYYY-MM'),

T2M:f.get('T2M'),

QV2M:f.get('QV2M'),

PS:f.get('PS'),

PBLTOP:f.get('PBLTOP'),

U10M:f.get('U10M'),

V10M:f.get('V10M')

});

});

return fc;

});


// ======================================================
// Merge Monthly Collections
// ======================================================

var allResults = ee.FeatureCollection(
monthlyCollections
).flatten();


// ======================================================
// Preview
// ======================================================

print("Total Records:",allResults.size());

print(allResults.first());


// ======================================================
// Export
// ======================================================

Export.table.toDrive({

collection:allResults,

description:'AQIVision_MERRA2_2015_2020_Optimized',

fileFormat:'CSV'

});
