// Batch Algae Cell Counter
// Automated counting of algae cells from brightfield microscopy images

setBatchMode(true); // Set batch mode to speed up processing and avoid displaying each image

dir = getDirectory("Choose a Directory"); // Set the directory where the images are stored

list = getFileList(dir); // Create a list of all the image files in the directory

for (i = 0; i < list.length; i++) { // Loop through the list of files
    if (endsWith(list[i], ".tif")) { // Only process TIFF images
        open(list[i]);
        run("Color Threshold...");
        setOption("BlackBackground", false);
        run("Convert to Mask");
        run("Make Binary");
        run("Fill Holes");
        run("Analyze Particles...", "size=20-infinity show=Masks display");
        close();
    }
}

setBatchMode(false); // Set batch mode back to false to enable GUI interactions
