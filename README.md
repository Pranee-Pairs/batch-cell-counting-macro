# ImageJ + Python Cell Analysis Pipeline

Automated pipeline for cell counting and size distribution analysis combining ImageJ automation with Python data visualization.

## Overview

This project demonstrates a complete bioimage analysis workflow:

1. **ImageJ Macro**: Batch processes microscopy images to count and measure cells
2. **Python Analysis**: Generates publication-ready histograms of cell size distributions

**Applications**: Cell size analysis, treatment comparisons, automated morphometry

## Workflow

```
Raw Microscopy Images → ImageJ Macro → Results.csv → Python Script → Size Distribution Plots
```

## ImageJ Component

**Location**: `imagej_macro/`

**Features**:
- Batch processes multiple TIFF images
- Automated color thresholding and particle analysis  
- Filters particles >20 pixels (removes debris)
- Outputs measurements to Results table for manual saving

**Usage**:
1. Open ImageJ/Fiji
2. Install macro: Plugins → Macros → Install...
3. Run macro and select folder containing TIFF images
4. Save Results table as CSV when processing complete

## Python Analysis Component

**Location**: `python_analysis/`

**Features**:
- Batch processes multiple CSV files automatically
- Calculates equivalent circular diameters from measured areas
- Generates separate histograms for areas and diameters
- Custom binning for optimal visualization
- High-resolution output (600 DPI) suitable for publication
- Proper scientific units (μm² and μm)

**Key Calculations**:
- Equivalent diameter: `d = 2 × √(Area/π)`
- Custom bin sizing for optimal histogram appearance

## Example Data

**Location**: `examples/`

**Input**: Brightfield microscopy images of cells at 100x magnification

**Output**: 
- Area distribution histograms (μm²)
- Diameter distribution histograms (μm)

**Note**: Set scale in ImageJ using microscope scale bar before analysis for accurate measurements in micrometers.

## Technical Notes

- **ImageJ macro** optimized for cells in brightfield microscopy
- **Python script** uses automatic binning based on data range
- **Unicode symbols** for proper scientific notation (μm², μm)
- **Memory management** with `plt.clf()` to prevent memory leaks during batch processing

## Applications

This pipeline can be adapted for:
- Cell size analysis across different treatments
- Morphological changes over time
- Quality control in cell culture
- Comparative studies between cell populations

## License

This project is licensed under the MIT License.
