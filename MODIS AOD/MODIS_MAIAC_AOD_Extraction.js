/*******************************************************
 AQIVision Project
 MODIS MAIAC AOD Extraction
 Google Earth Engine JavaScript

 Objective:
 Extract monthly Aerosol Optical Depth (AOD550)
 for all AQIVision cities from
 January 2015 to June 2020.

 Dataset:
 MODIS/061/MCD19A2_GRANULES

 Output:
 AQIVision_Monthly_AOD_2015_2020.csv
********************************************************/


// ======================================================
// Load City Feature Collection
// ======================================================

// Replace with your uploaded Earth Engine asset
var cities = ee.FeatureCollection(
    'projects/aqivision/assets/aqivision_cities'
);


// ======================================================
// Study Period
// ======================================================

var startDate = ee.Date('2015-01-01');
var endDate   = ee.Date('2020-07-01');


// Number of months
var totalMonths = endDate.difference(startDate, 'month');

print('Total Months:', totalMonths);


// ======================================================
// MODIS MAIAC Collection
// ======================================================

var modis = ee.ImageCollection('MODIS/061/MCD19A2_GRANULES');

print('MODIS Collection:', modis);


// ======================================================
// Monthly AOD Extraction
// ======================================================

var monthlyCollections = ee.List.sequence(
    0,
    totalMonths.subtract(1)
).map(function(m){

    m = ee.Number(m);

    var start = startDate.advance(m, 'month');
    var end   = start.advance(1, 'month');

    // Monthly mean AOD
    var monthlyImage = modis
        .filterDate(start, end)
        .select('Optical_Depth_055')
        .mean();

    // Extract AOD for every city
    var fc = monthlyImage.reduceRegions({

        collection: cities,

        reducer: ee.Reducer.mean(),

        scale: 1000

    });

    // Keep only required attributes
    fc = fc.map(function(feature){

        return ee.Feature(null, {

            City: feature.get('City'),

            Month: start.format('YYYY-MM'),

            AOD_550: feature.get('mean')

        });

    });

    return fc;

});


// ======================================================
// Merge Monthly Feature Collections
// ======================================================

var allResults = ee.FeatureCollection(
    monthlyCollections
).flatten();


// ======================================================
// Preview Results
// ======================================================

print('Total Records:', allResults.size());

print('First Record:', allResults.first());


// ======================================================
// Export to Google Drive
// ======================================================

Export.table.toDrive({

    collection: allResults,

    description: 'AQIVision_Monthly_AOD_2015_2020',

    fileFormat: 'CSV'

});
