# ImageJ Algae Cell Counter

Automated batch processing macro for counting algae cells in brightfield microscopy images.

## Description
This ImageJ macro processes multiple TIFF images to automatically detect and count algae cells using color thresholding and particle analysis. Results are displayed in ImageJ's Results table for manual saving.

## Requirements
- ImageJ or Fiji
- TIFF format images (.tif)
- **Recommended**: Set scale using your microscope's scale bar before running for accurate measurements

## How to Use
1. Open ImageJ/Fiji
2. Set scale (optional): Analyze → Set Scale
3. Install macro: Plugins → Macros → Install...
4. Run the macro: Plugins → Macros → [macro name]
5. Select folder containing your TIFF images
6. After processing, save results: File → Save As... or copy data from Results table

## What It Does
- Processes all TIFF images in selected folder
- Applies color thresholding to separate cells from background
- Converts to binary image and fills holes
- Detects particles (cells) larger than 20 pixels
- Displays all measurements in Results table

## Output Measurements
- **Area**: Cell area
- **Circularity**: How round the cell is (1.0 = perfect circle)  
- **AR**: Aspect ratio of fitted ellipse
- **Round**: Roundness measure
- **Solidity**: How "filled" the cell shape is

## Notes
- Optimized for algae cells in brightfield microscopy at 100x magnification
- Filters out particles smaller than 20 pixels to exclude debris
- May need threshold adjustment for different lighting conditions
- Works best with consistent imaging conditions

## Example
Input: Folder of brightfield microscopy images showing algae cells
Output: Results table with measurements for all detected cells across all images

## License
MIT License
