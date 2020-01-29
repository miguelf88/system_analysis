# Import system modules
import arcpy

# Set environment settings
arcpy.env.workspace = r"D:\Project Data\System Analysis\Jan 2020\Sys_analysis_2020\Sys_analysis_2020.gdb"
table = "single_market_area_no_urban_working_intersect"

# Add Fields
arcpy.AddField_management(in_table=table,
                          field_name="total_pop_intersect",
                          field_type="SHORT")
arcpy.AddField_management(in_table=table,
                          field_name="white_only_pop_intersect",
                          field_type="SHORT")
arcpy.AddField_management(in_table=table,
                          field_name="no_vehicle_hh_intersect",
                          field_type="SHORT")
arcpy.AddField_management(in_table=table,
                          field_name="under18_pop_intersect",
                          field_type="SHORT")
arcpy.AddField_management(in_table=table,
                          field_name="over65_pop_intersect",
                          field_type="SHORT")
arcpy.AddField_management(in_table=table,
                          field_name="poverty_hh_intersect",
                          field_type="SHORT")
arcpy.AddField_management(in_table=table,
                          field_name="total_hh_intersect",
                          field_type="SHORT")
arcpy.AddField_management(in_table=table,
                          field_name="minority_pop_intersect",
                          field_type="SHORT")

# Calculate newly added fields
arcpy.CalculateFields_management(in_table=table,
                                 expression_type="PYTHON3",
                                 fields=[["total_pop_intersect", "!demographic_data_total_pop! * (!Shape_Area!/!na_va_tracts_tract_area!)"],
                                         ["white_only_pop_intersect", "!demographic_data_white_only_pop! * (!Shape_Area!/!na_va_tracts_tract_area!)"],
                                         ["no_vehicle_hh_intersect", "!demographic_data_hh_no_vehcile! * (!Shape_Area!/!na_va_tracts_tract_area!)"],
                                         ["under18_pop_intersect", '!demographic_data_under18_pop! * (!Shape_Area!/!na_va_tracts_tract_area!)'],
                                         ["over65_pop_intersect", "!demographic_data_F65over_pop! * (!Shape_Area!/!na_va_tracts_tract_area!)"],
                                         ["poverty_hh_intersect", "!demographic_data_hh_poverty! * (!Shape_Area!/!na_va_tracts_tract_area!)"],
                                         ["total_hh_intersect", "!demographic_data_total_hh! * (!Shape_Area!/!na_va_tracts_tract_area!)"],
                                         ["minority_pop_intersect", "!demographic_data_minority_pop! * (!Shape_Area!/!na_va_tracts_tract_area!)"]])

# Dissolve the layer and sum up the demographic data
output_table = "single_market_area_no_urban_dissolve"
arcpy.Dissolve_management(table, output_table,
                          statistics_fields=[["total_pop_intersect", "SUM"],
                                             ["white_only_pop_intersect", "SUM"],
                                             ["no_vehicle_hh_intersect", "SUM"],
                                             ["under18_pop_intersect", "SUM"],
                                             ["over65_pop_intersect", "SUM"],
                                             ["poverty_hh_intersect", "SUM"],
                                             ["total_hh_intersect", "SUM"],
                                             ["minority_pop_intersect", "SUM"]])
