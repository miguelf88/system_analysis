###############################################
##     Iterates through a feature class      ##
##  And returns a KML file for each feature  ##
###############################################

import arcpy

# Define variables
fc_in = r"D:\Project Data\System Analysis\Jan 2020\Sys_analysis_2020\Sys_analysis_2020.gdb\multiple_market_areas_working_with_urban"
rideshed = 'rideshed'
out_folder = r'D:\Project Data\System Analysis\Jan 2020\KML Files'

# create list of unique rideshed names
lst_shed = list(set([r[0] for r in arcpy.da.SearchCursor(fc_in, (rideshed))]))

# loop through list
for rideshed_name in lst_shed:
    fld = arcpy.AddFieldDelimiters(fc_in, rideshed)
    where ="{0} = '{1}'".format(fld, rideshed_name)
    arcpy.MakeFeatureLayer_management(fc_in, "lyr", where)
    kmz_file = os.path.join(out_folder, "single_area_{0}.kmz".format(rideshed_name))
    arcpy.LayerToKML_conversion("lyr", kmz_file)
