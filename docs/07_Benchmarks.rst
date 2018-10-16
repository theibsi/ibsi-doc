Benchmarks
==========

This chapter presents the feature benchmark values for the digital
phantom and radiomics phantom. Features based on texture matrices
determined by slice and then fully merged (Figures
[figGLCMCalcApproaches]c and [figGLSZMCalcApproaches]b) were not
benchmarked, as this approach was not used. The list of benchmark values
is also available as a separate *.csv* table.

A tolerance was determined for the benchmark values in the radiomics
phantom, as minor differences introduced during image processing may
lead to different feature values. For this purpose the image data and
the mask were rotated (from :math:`-15^\circ` to :math:`15^\circ` in
:math:`5^\circ` steps) and translated (:math:`0.0`, :math:`0.25`,
:math:`0.50` and :math:`0.75` times the voxel spacing) in the
:math:`xy`-plane, and the ROI mask was eroded (2mm), kept the same, and
dilated (2mm). This lead to 336 values for a single feature. The
tolerance shown in the tables in this chapter is equal 5% of the
interquartile range of these values.

Additionally, it should be noted that all benchmarks are values actually
produced by teams involved in the IBSI, rather than averages. All
contributed values were rounded to 3 significant digits before being
processed and analysed to determine consensus.
