Radiomics phantom diagnostic features
=====================================

Assessing the diagnostic features for the radiomics phantom may assist
in identifying issues with regards to image processing. Minor deviations
to the values presented in this chapter may occur due to rounding
errors, or slightly different algorithmic implementations.

Characteristics of the original image
-------------------------------------

The characteristics of the original image, by definition, are the same
for all configurations.

Characteristics of the interpolated image
-----------------------------------------

*Mean*, *minimum* and *maximum* intensity may deviate due to differences
in how the original image is padded to determine the value of voxels at
the edge of the interpolation grid. As we are dealing with a CT data
set, it is also important to round intensities to the nearest integer
after interpolation.

Characteristics of the original ROI mask
----------------------------------------

Voxel counts of the ROI mask may deviate slightly due to differences in
algorithm implementation. Different IBSI participants reported :math:`1`
voxel more or less than the numbers provided below.

Characteristics of the interpolated ROI mask
--------------------------------------------

Interpolation is a critical step in the image processing scheme. When
performing interpolation, it is important to keep the points mentioned
in section [sec\_benchmark\_interpolation\_notes] in mind. Deviations in
the ROI mask voxel count are likely to occur if interpolation is
performed differently.

Characteristics of the re-segmented ROI mask
--------------------------------------------

These are the characteristics of the ROI masks within which the features
are subsequently calculated.

.. |Approaches to calculating grey level co-occurrence matrix-based features. :math:`\mathbf{M}_{\Delta k}` are texture matrices calculated for direction :math:`\Delta` in slice :math:`k` (if applicable), and :math:`f_{\Delta k}` is the corresponding feature value. In (b), (c) and (e) the matrices are merged prior to feature calculation.| image:: ./Figures/ApproachBySliceDirTexture.pdf
.. |Approaches to calculating grey level co-occurrence matrix-based features. :math:`\mathbf{M}_{\Delta k}` are texture matrices calculated for direction :math:`\Delta` in slice :math:`k` (if applicable), and :math:`f_{\Delta k}` is the corresponding feature value. In (b), (c) and (e) the matrices are merged prior to feature calculation.| image:: ./Figures/ApproachBySliceDirTextureMerge.pdf
.. |Approaches to calculating grey level co-occurrence matrix-based features. :math:`\mathbf{M}_{\Delta k}` are texture matrices calculated for direction :math:`\Delta` in slice :math:`k` (if applicable), and :math:`f_{\Delta k}` is the corresponding feature value. In (b), (c) and (e) the matrices are merged prior to feature calculation.| image:: ./Figures/ApproachBySliceDirTextureMergeBySlice.pdf
.. |Approaches to calculating grey level co-occurrence matrix-based features. :math:`\mathbf{M}_{\Delta k}` are texture matrices calculated for direction :math:`\Delta` in slice :math:`k` (if applicable), and :math:`f_{\Delta k}` is the corresponding feature value. In (b), (c) and (e) the matrices are merged prior to feature calculation.| image:: ./Figures/ApproachByVolumeDirTexture.pdf
.. |Approaches to calculating grey level co-occurrence matrix-based features. :math:`\mathbf{M}_{\Delta k}` are texture matrices calculated for direction :math:`\Delta` in slice :math:`k` (if applicable), and :math:`f_{\Delta k}` is the corresponding feature value. In (b), (c) and (e) the matrices are merged prior to feature calculation.| image:: ./Figures/ApproachByVolumeDirTextureMerge.pdf
.. |Approaches to calculating grey level size zone matrix-based features. :math:`\mathbf{M}_{k}` are texture matrices calculated for slice :math:`k` (if applicable), and :math:`f_{k}` is the corresponding feature value. In (b) the matrices from the different slices are merged prior to feature calculation.| image:: ./Figures/ApproachBySliceTexture.pdf
.. |Approaches to calculating grey level size zone matrix-based features. :math:`\mathbf{M}_{k}` are texture matrices calculated for slice :math:`k` (if applicable), and :math:`f_{k}` is the corresponding feature value. In (b) the matrices from the different slices are merged prior to feature calculation.| image:: ./Figures/ApproachBySliceTextureMerge.pdf
.. |Approaches to calculating grey level size zone matrix-based features. :math:`\mathbf{M}_{k}` are texture matrices calculated for slice :math:`k` (if applicable), and :math:`f_{k}` is the corresponding feature value. In (b) the matrices from the different slices are merged prior to feature calculation.| image:: ./Figures/ApproachByVolumeTexture.pdf

