from osgeo import gdal

# Example coordinates for a point in Berlin
longitude = 13.4050
latitude = 52.5200

# Open raster dataset
ds = gdal.Open(r"C:\Study\GIS\Tools&Data\srtm_germany_dtm\srtm_germany_dtm.tif")

# Get GeoTransform and Projection information
# Gives array with upper left coordinate, pixel size for x and y
gt = ds.GetGeoTransform()

# Convert to pixel coordinates with ratio and size of pixel and rounding
x_pixel = int((longitude - gt[0]) / gt[1])
y_pixel = int((gt[3] - latitude) / -gt[5])

# Fetch the band that you want to read from
band = ds.GetRasterBand(1)

# Read pixel data as 2D array - parameters are: x_pixel, y_pixel, window size x, window size y
value = band.ReadAsArray(x_pixel, y_pixel, 1, 1)

# Close the dataset
ds = None

# Print the pixel value
print(f'The pixel value at location {longitude}, {latitude} is: {value[0][0]}m')
# Output: The pixel value at location 13.405, 52.52 is: 48m