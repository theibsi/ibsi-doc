Image biomarker reporting guidelines
====================================

Reliable and complete reporting is necessary to ensure reproducibility
and validation of results. To help provide a complete report on image
processing and image biomarker extraction, we present the guidelines
below, as well as a nomenclature system to uniquely features.

Reporting guidelines
--------------------

These guidelines are partially based on the work of
:cite:`Sollini2017`. Additionally, guidelines are derived
from the image processing and feature calculation steps described within
this document. An earlier version was reported elsewhere
:cite:`vallieres2017responsible`.

.. list-table::
   :widths: auto

   * -  imaging 
     -  Describe which type of imaging was acquired, e.g. CT, PET.
   * -  acquisition 
     -  Describe image acquisition details, i.e. scanner vendor,  method of image acquisition (e.g. dynamic, contrast-enhanced),  contrast agents, molecular labels and stainings, as well as image  acquisition parameters (e.g. MR TE times, CT tube voltage and  current).
   * -  reconstruction 
     -  Describe how images were reconstructed from the  acquired data, e.g. (iterative) reconstruction algorithm parameters  and voxel dimensions.
   * -  approach 
     -  Describe whether the image volume is analysed  slice-by-slice (2D), or as a volume (3D).
   * -  process workflow 
     -  Describe the sequence of image processing steps  used for the analysis, preferably schematically.
   * -  software 
     -  Describe which software (if any) or in-house code was used  to perform image processing and feature extraction.
   * -  data availability 
     -  Describe whether and where (image) data, ROIs and  software code is made available.
   * -  procedure 
     -  Describe how data was converted from reconstructed image  data, e.g. by calculation of standard uptake values for PET.  References to algorithms should be provided, or otherwise described in  detail.
   * -  procedure 
     -  Describe post-processing steps and parameters, e.g.  field-of-view illumination correction in microscopy, noise correction  in MRI and partial volume effect correction in PET. References to  algorithms should be provided, or otherwise described in detail.
   * -  ROI 
     -  Describe which regions of interest were delineated and used for  analysis, e.g. specific organs, specific cells, primary tumours.
   * -  procedure 
     -  Describe how regions of interest were delineated in the  image. Specify if segmentation was performed manually, semi-automated  or fully automated, by how many users/experts, and how consensus was  formed (if applicable). Algorithms and settings used should be listed.
   * -  voxel dimensions 
     -  Specify original and interpolated voxel dimensions.
   * -  image interpolation method 
     -  Specify interpolation method used, e.g.  *trilinear interpolation*. Specify how original and interpolation  grids were aligned.
   * -  image intensity rounding 
     -  Specify rounding procedures for non-integer  interpolated grey levels (if applicable).
   * -  ROI interpolation method 
     -  Specify interpolation method used to  interpolate ROI morphological and intensity masks.
   * -  ROI partial volume 
     -  Specify minimum partial volume fraction required  to include an interpolated ROI mask voxel in the interpolated ROI (if  applicable).
   * -  ROI mask criteria 
     -  Specify which criteria were used to include or  exclude voxels from an ROI mask (if applicable).
   * -  discretisation method 
     -  Specify which method is being used for  discretising image intensities. References to the method should be  provided, or otherwise described in detail.
   * -  discretisation parameters 
     -  Specify discretisation parameters for  discretisation, e.g. number of bins or bin width.
   * -  feature set 
     -  Report which features were calculated. References to  feature definitions should be provided, or otherwise described in  detail.
   * -  feature parameters 
     -  Describe specific settings used for feature  calculation, e.g. the distance setting and matrix merging method for  the grey level co-occurrence matrix.
   * -  standardisation 
     -  State whether image processing and feature  calculation were tested on the digital phantom and the radiomics  phantom data. State whether the feature values calculated match the  IBSI benchmark values; otherwise state which ones do not match  benchmark values, and indicate why.

Feature nomenclature
--------------------

Image features may be extracted using a variety of different settings,
and may even share the same name. A feature nomenclature is thus
required. Let us take the example of differentiating the following
features: *i*) intensity histogram-based entropy, discretised using a
*fixed bin size* algorithm with 25 HU bins, extracted from a CT image;
and *ii*) grey level run length matrix entropy, discretised using a
*fixed bin number* algorithm with 32 bins, extracted from a PET image.
To refer to both as *entropy* would be ambiguous, whereas to add a full
textual description would be cumbersome. In the nomenclature proposed
below, the features would be called *entropy\ :sub:`IH, CT, FBS:25HU`*
and *entropy\ :sub:`RLM, PET, FBN:32`*, respectively.

Features are thus indicated by a feature name and a subscript. As the
nomenclature is designed to both concise and complete, only details for
which ambiguity may exist are to be explicitly incorporated in the
subscript. The subscript of a feature name may contain the following
items to address ambiguous naming:

#. An abbreviation of the feature family (required).

#. The aggregation method of a feature (optional).

#. A descriptor describing the modality the feature is based on, the
   specific channel (for microscopy images), the specific imaging data
   (in the case of repeat imaging or delta-features) sets, conversions
   (such as SUV and SUL), and/or the specific ROI. For example, one
   could write *PET:SUV* to separate it from *CT* and *PET:SUL* features
   (optional).

#. Spatial filters and settings (optional).

#. The interpolation algorithm and uniform interpolation grid spacing
   (optional).

#. The re-segmentation range and outlier filtering (optional).

#. The discretisation method and relevant discretisation parameters,
   i.e. number of bins or bin size (optional).

#. Feature specific parameters, such as distance for some texture
   features (optional).

Optional descriptors are only added to the subscript if there are
multiple possibilities. For example, if only CT data is used, adding the
modality to the subscript is not required. Nonetheless, such details
must be reported as well (see section [sec\_reporting\_guidelines]).

The sections below have tables with permanent IBSI identifiers for
concepts that were defined within this document.

Abbreviating feature families
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The following is a list of the feature families in the document and
their suggested abbreviations:

.. list-table::
   :widths: auto

   * -  morphology 
     -  MORPH 
     - 
   * -  local intensity 
     -  LI 
     - 
   * -  intensity-based statistics 
     -  IS, STAT 
     - 
   * -  intensity histogram 
     -  IH 
     - 
   * -  intensity-volume histogram 
     -  IVH 
     - 
   * -  grey level co-occurrence matrix 
     -  GLCM, CM 
     - 
   * -  grey level run length matrix 
     -  GLRLM, RLM 
     - 
   * -  grey level size zone matrix 
     -  GLSZM, SZM
     - 
   * -  grey level distance zone matrix 
     -  GLDZM, DZM 
     - 
   * -  neighbourhood grey tone difference matrix 
     -  NGTDM 
     - 
   * -  neighbouring grey level dependence matrix 
     -  NGLDM 
     - 

Abbreviating feature aggregation
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The following is a list of feature families and the possible aggregation
methods:

.. list-table::
   :widths: auto

   * -  – 
     -  features are 3D by definition 
     - 
   * -  2D 
     -  averaged over slices (rare) 
     - 
   * -  –, 3D 
     -  calculated over the volume (default) 
     - 
   * -  2D:avg 
     -  averaged over slices and directions 
     - 
   * -  2D:mrg, 2D:smrg 
     -  merged directions per slice and averaged
     - 
   * -  2D:vmrg 
     -  merged over all slices (rare)
     - 
   * -  3D:avg 
     -  averaged over 3D directions
     - 
   * -  3D:mrg 
     -  merged 3D directions
     - 
   * -  2D, 2D:avg 
     -  averaged over slices 
     - 
   * -  2D:mrg 
     -  merged over all slices (rare) 
     - 
   * -  3D 
     -  calculated from single 3D matrix 
     - 

In the list above, ’–’ signifies an empty entry which does not need to
be added to the subscript. The following examples highlight the
nomenclature used above:

-  joint maximum\ :sub:`CM, 2D:avg`: GLCM-based *joint maximum* feature,
   calculated by averaging the feature for every in-slice GLCM.

-  short runs emphasis\ :sub:`RLM, 3D:mrg`: RLM-based *short runs
   emphasis* feature, calculated from an RLM that was aggregated by
   merging the RLM of each 3D direction.

-  mean\ :sub:`IS`: intensity statistical *mean* feature, calculated
   over the 3D ROI volume.

-  grey level variance\ :sub:`SZM, 2D`: SZM-based *grey level variance*
   feature, calculated by averaging the feature value from the SZM in
   each slice over all the slices.

Abbreviating interpolation
^^^^^^^^^^^^^^^^^^^^^^^^^^

The following is a list of interpolation methods and the suggested
notation. Note that # is the interpolation spacing, including units, and
*dim* is 2D for interpolation with the slice plane and 3D for volumetric
interpolation.

.. list-table::
   :widths: auto

   * -  to 0.8 **interpolation method** 
     -  **notation**
   * -  none 
     -  INT:–
   * -  nearest neighbour interpolation 
     -  NNB:\ *dim*:#
   * -  linear interpolation 
     -  LIN:\ *dim*:#
   * -  cubic convolution interpolation 
     -  CCI:\ *dim*:#
   * -  cubic spline interpolation 
     -  CSI:\ *dim*:#, SI3:\ *dim*:#

The dimension attribute and interpolation spacing may be omitted if this
is clear from the context. The following examples highlight the
nomenclature introduced above:

-  mean\ :sub:`IS, LIN:2D:2mm`: intensity statistical *mean* feature,
   calculated after *bilinear* interpolation with the slice planes to
   uniform voxel sizes of 2mm.

-  mean\ :sub:`IH, NNB:3D:1mm`: intensity histogram *mean* feature,
   calculated after *trilinear* interpolation to uniform voxel sizes of
   1mm.

-  joint maximum\ :sub:`CM, 2D:mrg, CSI:2D:2mm`: GLCM-based *joint
   maximum* feature, calculated by first merging all GLCM within a slice
   to single GLCM, calculating the feature and then averaging the
   feature values over the slices. GLCMs were determined in the image
   interpolated within the slice plane to 2 :math:`\times` 2mm voxels
   using *cubic spline* interpolation.

Describing re-segmentation
^^^^^^^^^^^^^^^^^^^^^^^^^^

Re-segmentation can be noted as follows:

.. list-table::
   :widths: auto

   * -  none 
     -  RS:– 
     - 
   * -  range 
     -  RS:[#,#] 
     - 
   * -  outlier filtering 
     -  RS:#\ :math:`\sigma` 
     - 

In the table above # signify numbers. A re-segmentation range can be
half-open, i.e. RS:[#,\ :math:`\infty`). Re-segmentation methods may
moreover be chained, i.e. both range and outlier filtering methods may
be used in sequence. This is noted as RS:[#,#]+#\ :math:`\sigma`, when
range re-segmentation takes place before applying an outlier threshold,
and RS:#\ :math:`\sigma`\ +[#,#] vice versa. The following are examples
of the application of the above notation:

-  mean\ :sub:`IS, CT, RS:[-200,150]`: intensity statistical *mean*
   feature, based on an ROI in a CT image that was re-segmented within a
   [-200,150] HU range.

-  mean\ :sub:`IS, PET:SUV, RS:[3,\ :math:`\infty`)`: intensity
   statistical *mean* feature, based on an ROI in a PET image with SUV
   values, that was re-segmented to contain only SUV of 3 and above.

-  mean\ :sub:`IS, MRI:T1, RS:3\ :math:`\sigma``: intensity statistical
   *mean* feature, based on an ROI in a T1-weighted MR image where the
   ROI was re-segmented by removing voxels with an intensity outside a
   :math:`\mu \pm 3\sigma` range.

Abbreviating discretisation
^^^^^^^^^^^^^^^^^^^^^^^^^^^

The following is a list of discretisation methods and the suggested
notation. Note that # is the value of the relevant discretisation
parameter, e.g. number of bins or bin size, including units.

.. list-table::
   :widths: auto

   * -  to 0.8 **discretisation method** 
     -  **notation** 
     - 
   * -  none 
     -  DIS:– 
     - 
   * -  fixed bin size 
     -  FBS:# 
     - 
   * -  fixed bin number 
     -  FBN:# 
     - 
   * -  histogram equalisation 
     -  EQ:#
     - 
   * -  Lloyd-Max, minimum mean squared 
     -  LM:#, MMS:# 
     - 

In the table above, # signify numbers such as the number of bins or
their width. Histogram equalisation of the ROI intensities can be
performed before the “none”, “fixed bin size”, “fixed bin number” or
“Lloyd-Max, minimum mean squared” algorithms defined above, with #
specifying the number of bins in the histogram to be equalised. The
following are examples of the application of the above notation:

-  mean\ :sub:`IH,PET:SUV,RS[0,\ :math:`\infty`],FBS:0.2`: intensity
   histogram *mean* feature, based on an ROI in a SUV-PET image, with
   bin-width of 0.2 SUV, and binning from 0.0 SUV.

-  grey level variance\ :sub:`SZM,MR:T1,RS:3\ :math:`\sigma`,FBN:64`:
   size zone matrix-based *grey level variance* feature, based on an ROI
   in a T1-weighted MR image, with :math:`3\sigma` re-segmentation and
   subsequent binning into 64 bins.

Abbreviating feature-specific parameters
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Some features and feature families require additional parameters, which
may be varied. These are the following:

.. list-table::
   :widths: auto

   * -  –, SYM 
     -  symmetrical co-occurrence matrices 
     - 
   * -  ASYM 
     -  asymmetrical co-occurrence matrices (not recommended) 
     - 
   * -  :math:`\delta`:#, :math:`\delta`-:math:`\infty`:# 
     -  Chebyshev  (:math:`\ell_{\infty}`) norm with distance # (default) 
     - 
   * -  :math:`\delta`-:math:`2`:# 
     -  Euclidean (:math:`\ell_{2}`) norm with  distance # 
     - 
   * -  :math:`\delta`-:math:`1`:# 
     -  Manhattan (:math:`\ell_{1}`) norm with  distance # 
     - 
   * -  –, w:1 
     -  no weighting (default) 
     - 
   * -  w:f 
     -  weighting with function :math:`f` 
     - 
   * -  –, w:1 
     -  no weighting (default) 
     - 
   * -  w:f 
     -  weighting with function :math:`f` 
     - 
   * -  :math:`\delta`:#, :math:`\delta`-:math:`\infty`:# 
     -  Chebyshev  (:math:`\ell_{\infty}`) norm with distance (default) # 
     - 
   * -  :math:`\delta`-:math:`2`:# 
     -  Euclidean (:math:`\ell_{2}`) norm with  distance # 
     - 
   * -  :math:`\delta`-:math:`1`:# 
     -  Manhattan (:math:`\ell_{1}`) norm with  distance # 
     - 
   * -  :math:`\delta`:#, :math:`\delta`-:math:`\infty`:# 
     -  Chebyshev  (:math:`\ell_{\infty}`) norm with distance (default) # 
     - 
   * -  :math:`\delta`-:math:`2`:# 
     -  Euclidean (:math:`\ell_{2}`) norm with  distance # 
     - 
   * -  :math:`\delta`-:math:`1`:# 
     -  Manhattan (:math:`\ell_{1}`) norm with  distance # 
     - 
   * -  –, :math:`l`-:math:`\infty`:# 
     -  Chebyshev (:math:`\ell_{\infty}`) norm  
     - 
   * -  :math:`l`-:math:`2`:# 
     -  Euclidean (:math:`\ell_{2}`) norm 
     - 
   * -  :math:`l`-:math:`1`:# 
     -  Manhattan (:math:`\ell_{1}`) norm (default) 
     - 
   * -  :math:`\delta`:#, :math:`\delta`-:math:`\infty`:# 
     -  Chebyshev  (:math:`\ell_{\infty}`) norm with distance # (default) 
     - 
   * -  :math:`\delta`-:math:`2`:# 
     -  Euclidean (:math:`\ell_{2}`) norm with  distance # 
     - 
   * -  :math:`\delta`-:math:`1`:# 
     -  Manhattan (:math:`\ell_{1}`) norm with  distance # 
     - 
   * -  –, w:1 
     -  no weighting (default) 
     - 
   * -  w:f 
     -  weighting with function :math:`f` 
     - 
   * -  :math:`\alpha`:# 
     -  dependence coarseness parameter with value # 
     - 
   * -  :math:`\delta`:#, :math:`\delta`-:math:`\infty`:# 
     -  Chebyshev  (:math:`\ell_{\infty}`) norm with distance # (default) 
     - 
   * -  :math:`\delta`-:math:`2`:# 
     -  Euclidean (:math:`\ell_{2}`) norm with  distance # 
     - 
   * -  :math:`\delta`-:math:`1`:# 
     -  Manhattan (:math:`\ell_{1}`) norm with  distance # 
     - 
   * -  –, w:1 
     -  no weighting (default) 
     - 
   * -  w:f 
     -  weighting with function :math:`f` 
     - 

In the above table, # represents numbers.
