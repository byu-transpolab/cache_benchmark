# cache_benchmark
Data for a benchmark or sandbox travel model scenario in Cache Valley, Utah

## Motivation
The travel modeling community has long needed a benchmark scenario on which to implement and compare
model frameworks in a quantitative manner. For example, agencies often wish to know how improvements to
model sensitivity will affect model run time. This repository is intended to push us towards that
goal.

The focus of this exercise is specifically on *demand* models, and as such we are less concerned with 
the highway assignment steps. But these steps are critical for the interpretation and implementation of 
the demand model, so they cannot be ignored completely. Researchers who implement their models in this 
sandbox may use a whichever of the several network engines that they have available.

## Contents
This repository contains several files that researchers can draw upon to generate their own scenarios. 
The files are compiled from and for the trip-based model developed by Fehr & Peers for the Cache Valley 
Metropolitan Planning Organization (MPO), which oversees transportation planning efforts in the Logan, 
Utah metropolitan area. The files are provided courtesty of the Utah Department of Transportation 
and the Cache Valley MPO.

The first set of files are drawn from the inputs to the travel model:
  - A **Highway network** labeled with vehicle counts as well as the trip-based model vehicle forecasts
  - A **Transit network** with accompanying ridership measures
  - A topologically connected **Bicyle network**
  - A **Socioeconomic data** file with employment and aggregate household characteristics by TAZ.
  - A **Traffic Analysis Zone** geojson file

A second set of files are outputs of the travel model:
  - **Travel time matrices** 
  - **Passenger origin-destination matrices**
  - **Freight origin-destination matrices** 
  - **Internal/External trip matrices** 

These output files may be useful if researchers optionally wish to --- for example --- include freight
processes in the model steps or simply include them as background traffic.

A household travel survey for the region will be made available on request to creditable researchers. This survey
was conducted in Spring and Summer of 2023.

### File formats
In general, tabular data is provided as plain text with comma-separated values and names in a header; a data
dictionary supplied with the file provides more attributes.
Geospatial data are provided as geojson files, and matrix files are provided in an OMX format. Network files 
are given as node / link tables but will be supplied as GMNS files in the future.

## Report

If you implement the a model in this sandbox, we would kindly request for you to send us a report with the following information:
  - The name of the model and the organization behind the implementation.
  - The basic design of your model, including which elements are held constant with the Cache Valley model and
    any necessary information from the network or supply model.
  - Total model run time, broken down by model step and feedback cycle.
  - A report of model failure statistics
  - Assigned highway volumes at counted locations in a CSV file.
An example report is provided in this repository. 
