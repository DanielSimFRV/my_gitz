from batch_run_kdes import batch_run_kdes
import os
import arcpy

numerator_layers = arcpy.GetParameter(0)
denominator_layer = arcpy.GetParameter(1)
denominator_threshold = arcpy.GetParameter(4)

for cell_size in arcpy.GetParameter(2):
    for search_radius in arcpy.GetParameter(3):
        fgdb_locn = r"C:\Users\ri072731\Desktop\ArcGIS\PrepAVClinical"
        fgdb_name = "KDEs_{0}_{1}.gdb".format(search_radius, '{}'.format(cell_size).replace('.', 'p'))

        if not arcpy.Exists(os.path.join(fgdb_locn, fgdb_name)):
            arcpy.AddMessage("Creating FGDB {0}".format(fgdb_name))
            arcpy.management.CreateFileGDB(fgdb_locn, fgdb_name, "CURRENT")

        arcpy.AddMessage(f"search_radius = {search_radius} / cell_size = {cell_size}")
        arcpy.AddMessage("Writing to FGDB {0}".format(fgdb_name))

        batch_run_kdes(input_layers = numerator_layers,
            denominator_layer = denominator_layer, 
            kde_output_cell_size = cell_size, 
            kde_search_radius = search_radius, 
            kde_population_field = "weighting", 
            scale_normed_output = True, 
            winsorise_output = True, 
            winsor_lower_bound = 3, 
            winsor_upper_bound = 3, 
            output_fgdb = os.path.join(fgdb_locn, fgdb_name),
            denominator_threshold = denominator_threshold)
