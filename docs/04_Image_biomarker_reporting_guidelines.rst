.. _chap_report_guidelines:

Image biomarker reporting guidelines
====================================

Reliable and complete reporting is necessary to ensure reproducibility
and validation of results. To help provide a complete report on image
processing and image biomarker extraction, we present the guidelines
below, as well as a nomenclature system to uniquely features.

.. _sec_reporting_guidelines:

Reporting guidelines
--------------------

These guidelines are partially based on the work of
:raw-latex:`\citet{Sollini2017,Lambin2017,Sanduleanu2018-iu,Traverso2018-yr}`.
Additionally, guidelines are derived from the image processing and
feature calculation steps described within this document. An earlier
version was reported elsewhere
:cite:`vallieres2017responsible`.

.. raw:: latex

   \footnotesize{
   \begin{longtable}{p{3.5cm}ccp{7cm}}

   \toprule
   \textbf{topic} & & \textbf{item} & \textbf{description}\\
   \midrule
   \endhead

   \bottomrule
   \multicolumn{4}{r}{\textit{continued on next page}}
   \endfoot

   \bottomrule
   \caption[Reporting guidelines]{Guidelines for reporting on radiomic studies. Not all items may be applicable.} \label{table_guidelines}
   \endlastfoot

   \multicolumn{4}{l}{\textbf{Patient}}\\
   \midrule
   Region of interest\footnote{Also referred to as volume of interest.} & &
   1 & Describe the region of interest that is being imaged.
   \\
   Patient preparation & & 2a & Describe specific instructions given to
   patients prior to image acquisition, e.g. fasting prior to imaging.
   \\
   & & 2b & Describe administration of drugs to the patient prior to image
   acquisition, e.g. muscle relaxants. \\
   & & 2c & Describe the use of specific equipment for patient comfort
   during scanning, e.g. ear plugs. \\
   Radioactive tracer & PET, SPECT & 3a & Describe which radioactive tracer
   was administered to the patient, e.g. 18F-FDG. \\
   & PET, SPECT & 3b & Describe the administration method. \\
   & PET, SPECT & 3c & Describe the injected activity of the radioactive
   tracer at administration. \\
   & PET, SPECT & 3d & Describe the uptake time prior to image acquisition.
   \\
   & PET, SPECT & 3e & Describe how competing substance levels were
   controlled.\footnote{An example is glucose present in the blood which
     competes with the uptake of 18F-FDG tracer in tumour tissue. To reduce
     competition with the tracer, patients are usually asked to fast for
     several hours and a blood glucose measurement may be conducted prior
     to tracer administration.} \\
   Contrast agent & & 4a & Describe which contrast agent was administered
   to the patient. \\
   & & 4b & Describe the administration method. \\
   & & 4c & Describe the injected quantity of contrast agent.
   \\
   & & 4d & Describe the uptake time prior to image acquisition.
   \\
   & & 4e & Describe how competing substance levels were controlled.
   \\
   Comorbidities & & 5 & Describe if the patients have comorbidities that
   affect imaging.\footnote{An example of a comorbidity that may affect
     image quality in 18F-FDG PET scans are type I and type II diabetes
     melitus, as well as kidney failure.} \\
    
   \multicolumn{4}{l}{\textbf{Acquisition}\footnote{Many acquisition parameters may be
     extracted from DICOM header meta-data, or calculated from them.}}\\
   \midrule
   Acquisition protocol & & 6 & Describe whether a standard imaging
   protocol was used, and where its description may be found.
   \\
   Scanner type & & 7 & Describe the scanner type(s) and vendor(s) used in
   the study. \\
   Imaging modality & & 8 & Clearly state the imaging modality that was
   used in the study, e.g. CT, MRI. \\
   Static/dynamic scans & & 9a & State if the scans were static or dynamic.
   \\
   & Dynamic scans & 9b & Describe the acquisition time per time frame.
   \\
   & Dynamic scans & 9c & Describe any temporal modelling technique that
   was used. \\
   Scanner calibration & & 10 & Describe how and when the scanner was
   calibrated. \\
   Patient instructions & & 11 & Describe specific instructions given to
   the patient during acquisition, e.g. breath holding. \\
   Anatomical motion correction & & 12 & Describe the method used to
   minimise the effect of anatomical motion. \\
   Scan duration & & 13 & Describe the duration of the complete scan or the
   time per bed position. \\
   Tube voltage & CT & 14 & Describe the peak kilo voltage output of the
   X-ray source. \\
   Tube current & CT & 15 & Describe the tube current in mA.
   \\
   Time-of-flight & PET & 16 & State if scanner time-of-flight capabilities
   are used during acquisition. \\
   RF coil & MRI & 17 & Describe what kind RF coil used for acquisition,
   incl. vendor. \\
   Scanning sequence & MRI & 18a & Describe which scanning sequence was
   acquired. \\
   & MRI & 18b & Describe which sequence variant was acquired.
   \\
   & MRI & 18c & Describe which scan options apply to the current sequence,
   e.g. flow compensation, cardiac gating. \\
   Repetition time & MRI & 19 & Describe the time in ms between subsequent
   pulse sequences. \\
   Echo time & MRI & 20 & Describe the echo time in ms. \\
   Echo train length & MRI & 21 & Describe the number of lines in k-space
   that are acquired per excitation pulse. \\
   Inversion time & MRI & 22 & Describe the time in ms between the middle
   of the inverting RF pulse to the middle of the excitation pulse.
   \\
   Flip angle & MRI & 23 & Describe the flip angle produced by the RF
   pulses. \\
   Acquisition type & MRI & 24 & Describe the acquisition type of the MRI
   scan, e.g. 3D. \\
   k-space traversal & MRI & 25 & Describe the acquisition trajectory of
   the k-space. \\
   Number of averages/ excitations & MRI & 26 & Describe the number of
   times each point in k-space is sampled. \\
   Magnetic field strength & MRI & 27 & Describe the nominal strength of
   the MR magnetic field. \\

   \multicolumn{4}{l}{\textbf{Reconstruction}\footnote{Many reconstruction parameters may be
     extracted from DICOM header meta-data.}}\\
   \midrule
   In-plane resolution & & 28 & Describe the distance between pixels, or
   alternatively the field of view and matrix size. \\
   Image slice thickness & & 29 & Describe the slice thickness.
   \\
   Image slice spacing & & 30 & Describe the distance between image
   slices.\footnote{Spacing between image slicing is commonly, but not
     necessarily, the same as the slice thickness,.} \\
   Convolution kernel & CT & 31a & Describe the convolution kernel used to
   reconstruct the image. \\
   & CT & 31b & Describe settings pertaining to iterative reconstruction
   algorithms. \\
   Exposure & CT & 31c & Describe the exposure (in mAs) in slices
   containing the region of interest. \\
   Reconstruction method & PET & 32a & Describe which reconstruction method
   was used, e.g. 3D OSEM. \\
   & PET & 32b & Describe the number of iterations for iterative
   reconstruction. \\
   & PET & 32c & Describe the number of subsets for iterative
   reconstruction. \\
   Point spread function modelling & PET & 33 & Describe if and how
   point-spread function modelling was performed. \\
   Image corrections & PET & 34a & Describe if and how attenuation
   correction was performed. \\
   & PET & 34b & Describe if and how other forms of correction were
   performed, e.g. scatter correction, randoms correction, dead time
   correction etc. \\
   Reconstruction method & MRI & 35a & Describe the reconstruction method
   used to reconstruct the image from the k-space information.
   \\
   & MRI & 35b & Describe any artifact suppression methods used during
   reconstruction to suppress artifacts due to undersampling of k-space.
   \\
   Diffusion-weighted imaging & DWI-MRI & 36 & Describe the b-values used
   for diffusion-weighting. \\

   \multicolumn{4}{l}{\textbf{Image registration}}\\
   \midrule
   Registration method & & 37 & Describe the method used to register
   multi-modality imaging. \\

   \multicolumn{4}{l}{\textbf{Image processing - data conversion}} \\
   \midrule
   SUV normalisation & PET & 38 & Describe which standardised uptake value
   (SUV) normalisation method is used. \\
   ADC computation & DWI-MRI & 39 & Describe how apparent diffusion
   coefficient (ADC) values were calculated. \\
   Other data conversions & & 40 & Describe any other conversions that are
   performed to generate e.g. perfusion maps. \\

   \multicolumn{4}{l}{\textbf{Image processing - post-acquisition processing}} \\
   \midrule
   Anti-aliasing & & 41 & Describe the method used to deal with
   anti-aliasing when down-sampling during interpolation. \\
   Noise suppression & & 42 & Describe methods used to suppress image
   noise. \\
   Post-reconstruction smoothing filter & PET & 43 & Describe the width of
   the Gaussian filter (FWHM) to spatially smooth intensities.
   \\
   Skull stripping & MRI (brain) & 44 & Describe method used to perform
   skull stripping. \\
   Non-uniformity correction\footnote{Also known as bias-field correction.}
   & MRI & 45 & Describe the method and settings used to perform
   non-uniformity correction. \\
   Intensity normalisation & & 46 & Describe the method and settings used
   to normalise intensity distributions within a patient or patient cohort.
   \\
   Other post-acquisition processing methods & & 47 & Describe any other
   methods that were used to process the image and are not mentioned
   separately in this list. \\

   \multicolumn{4}{l}{\textbf{Segmentation}} \\
   \midrule
   Segmentation method & & 48a & Describe how regions of interest were
   segmented, e.g. manually. \\
   & & 48b & Describe the number of experts, their expertise and consensus
   strategies for manual delineation. \\
   & & 48c & Describe methods and settings used for semi-automatic and
   fully automatic segmentation. \\
   & & 48d & Describe which image was used to define segmentation in case
   of multi-modality imaging. \\
   Conversion to mask & & 49 & Describe the method used to convert
   polygonal or mesh-based segmentations to a voxel-based mask.
   \\

   \multicolumn{4}{l}{\textbf{Image processing - image interpolation}} \\
   \midrule
   Interpolation method & & 50a & Describe which interpolation algorithm
   was used to interpolate the image. \\
   & & 50b & Describe how the position of the interpolation grid was
   defined, e.g. align by center. \\
   & & 50c & Describe how the dimensions of the interpolation grid were
   defined, e.g. rounded to nearest integer. \\
   & & 50d & Describe how extrapolation beyond the original image was
   handled. \\
   Voxel dimensions & & 51 & Describe the size of the interpolated voxels.
   \\
   Intensity rounding & CT & 52 & Describe how fractional Hounsfield Units
   are rounded to integer values after interpolation. \\

   \multicolumn{4}{l}{\textbf{Image processing - ROI interpolation}} \\
   \midrule
   Interpolation method & & 53 & Describe which interpolation algorithm was
   used to interpolate the region of interest mask. \\
   Partially masked voxels & & 54 & Describe how partially masked voxels
   after interpolation are handled. \\

   \multicolumn{4}{l}{\textbf{Image processing - re-segmentation}} \\
   \midrule
   Re-segmentation methods & & 55 & Describe which methods and settings are
   used to re-segment the ROI intensity mask. \\

   \multicolumn{4}{l}{\textbf{Image processing - discretisation}} \\
   \midrule
   Discretisation method\footnote{Discretisation may be performed
     separately to create intensity-volume histograms. If this is indeed
     the case, this should be described as well.} & & 56a & Describe the
   method used to discretise image intensities. \\
   & & 56b & Describe the number of bins (FBN) or the bin size (FBS) used
   for discretisation. \\
   & & 56c & Describe the lowest intensity in the first bin for FBS
   discretisation.\footnote{This is typically set by range re-segmentation.}
   \\

   \multicolumn{4}{l}{\textbf{Image processing - image transformation}} \\
   \midrule
   Image filter\footnote{The IBSI has not introduced image transformation
     into the standardised image processing scheme, and is in the process
     of benchmarking various common filters. This section may therefore be
     expanded in the future.} & & 57 & Describe the methods and settings
   used to filter images, e.g. Laplacian-of-Gaussian. \\

   \multicolumn{4}{l}{\textbf{Image biomarker computation}} \\
   \midrule
   Biomarker set & & 58 & Describe which set of image biomarkers is
   computed and refer to their definitions or provide these.
   \\
   IBSI compliance & & 59 & State if the software used to extract the set
   of image biomarkers is compliant with the IBSI benchmarks.\footnote{A
     software is compliant if and only if it is able to reproduce the image
     biomarker benchmarks for the digital phantom and for one or more image
     processing configurations using the radiomics CT phantom. Reviewers
     may demand that you provide the IBSI compliance spreadsheet for your
     software.} \\
   Robustness & & 60 & Describe how robustness of the image biomarkers was
   assessed, e.g. test-retest analysis. \\
   Software availability & & 61 & Describe which software and version was
   used to compute image biomarkers. \\

   \multicolumn{4}{l}{\textbf{Image biomarker computation - texture parameters}}\\
   \midrule
   Texture matrix aggregation & & 62 & Define how texture-matrix based
   biomarkers were computed from underlying texture matrices.
   \\
   Distance weighting & & 63 & Define how CM, RLM, NGTDM and NGLDM weight
   distances, e.g. no weighting. \\
   CM symmetry & & 64 & Define whether symmetric or asymmetric
   co-occurrence matrices were computed. \\
   CM distance & & 65 & Define the (Chebyshev) distance at which
   co-occurrence of intensities is determined, e.g. 1. \\
   SZM linkage distance & & 66 & Define the distance and distance norm for
   which voxels with the same intensity are considered to belong to the
   same zone for the purpose of constructing an SZM, e.g. Chebyshev
   distance of 1. \\
   DZM linkage distance & & 67 & Define the distance and distance norm for
   which voxels with the same intensity are considered to belong to the
   same zone for the purpose of constructing a DZM, e.g. Chebyshev distance
   of 1. \\
   DZM zone distance norm & & 68 & Define the distance norm for determining
   the distance of zones to the border of the ROI, e.g. Manhattan distance.
   \\
   NGTDM distance & & 69 & Define the neighbourhood distance and distance
   norm for the NGTDM, e.g. Chebyshev distance of 1. \\
   NGLDM distance & & 70 & Define the neighbourhood distance and distance
   norm for the NGLDM, e.g. Chebyshev distance of 1. \\
   NGLDM coarseness & & 71 & Define the coarseness parameter for the NGLDM,
   e.g. 0. \\

   \multicolumn{4}{l}{\textbf{Machine learning and radiomics analysis}} \\
   \midrule
   Diagnostic and prognostic modelling & & 72 & See the TRIPOD guidelines
   for reporting on diagnostic and prognostic modelling. \\
   Comparison with known factors & & 73 & Describe where performance of
   radiomics models is compared with known (clinical) factors.
   \\
   Multicollinearity & & 74 & Describe where the multicollinearity between
   image biomarkers in the signature is assessed. \\
   Model availability & & 75 & Describe where radiomics models with the
   necessary pre-processing information may be found. \\
   Data availability & & 76 & Describe where imaging data and relevant
   meta-data used in the study may be found. \\
   \end{longtable}
   }

.. raw:: latex

   \FloatBarrier

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
below, the features would be called *entropy\ IH, CT, FBS:25HU* and
*entropy\ RLM, PET, FBN:32*, respectively.

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
must be reported as well (see section
`4.1 <#sec_reporting_guidelines>`__).

The sections below have tables with permanent IBSI identifiers for
concepts that were defined within this document.

Abbreviating feature families
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The following is a list of the feature families in the document and
their suggested abbreviations:

.. list-table::
   :widths: auto

   * -  to 0.99 **feature family** 
     -  **abbreviation** 
     - 
   * -  morphology 
     -  MORPH 
     -  **HCUG**
   * -  local intensity 
     -  LI 
     -  **9ST6**
   * -  intensity-based statistics 
     -  IS, STAT 
     -  **UHIW**
   * -  intensity histogram 
     -  IH 
     -  **ZVCW**
   * -  intensity-volume histogram 
     -  IVH 
     -  **P88C**
   * -  grey level co-occurrence matrix 
     -  GLCM, CM 
     -  **LFYI**
   * -  grey level run length matrix 
     -  GLRLM, RLM 
     -  **TP0I**
   * -  grey level size zone matrix 
     -  GLSZM, SZM
     -  **9SAK**
   * -  grey level distance zone matrix 
     -  GLDZM, DZM 
     -  **VMDZ**
   * -  neighbourhood grey tone difference matrix 
     -  NGTDM 
     -  **IPET**
   * -  neighbouring grey level dependence matrix 
     -  NGLDM 
     -  **REK0**

Abbreviating feature aggregation
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The following is a list of feature families and the possible aggregation
methods:

.. list-table::
   :widths: auto

   * -  – 
     -  features are 3D by definition 
     -  **DHQ4**
   * -  2D 
     -  averaged over slices (rare) 
     -  **3IDG**
   * -  –, 3D 
     -  calculated over the volume (default) 
     -  **DHQ4**
   * -  2D:avg 
     -  averaged over slices and directions 
     -  **BTW3**
   * -  2D:mrg, 2D:smrg 
     -  merged directions per slice and averaged 
     -  **SUJT**
   * -  2.5D:avg, 2.5D:dmrg 
     -  merged per direction and averaged 
     -  **JJUI**
   * -  2.5D:mrg, 2.5D:vmrg 
     -  merged over all slices
     -  **ZW7Z**
   * -  3D:avg 
     -  averaged over 3D directions
     -  **ITBB**
   * -  3D:mrg 
     -  merged 3D directions
     -  **IAZD**
   * -  2D 
     -  averaged over slices 
     -  **8QNN**
   * -  2.5D 
     -  merged over all slices 
     -  **62GR**
   * -  3D 
     -  calculated from single 3D matrix 
     -  **KOBO**

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
     -  **USB3**
   * -  outlier filtering 
     -  RS:#\ :math:`\sigma` 
     -  **7ACA**

In the table above # signify numbers. A re-segmentation range can be
half-open, i.e. RS:[#,\ :math:`\infty`). Re-segmentation methods may be
combined, i.e. both range and outlier filtering methods may be used.
This is noted as RS:[#,#]+#\ :math:`\sigma` or
RS:#\ :math:`\sigma`\ +[#,#]. The following are examples of the
application of the above notation:

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
     -  **Q3RU**
   * -  fixed bin number 
     -  FBN:# 
     -  **K15C**
   * -  histogram equalisation 
     -  EQ:#
     - 
   * -  Lloyd-Max, minimum mean squared 
     -  LM:#, MMS:# 
     - 

In the table above, # signify numbers such as the number of bins or
their width. Histogram equalisation of the ROI intensities can be
performed before the "none", "fixed bin size", "fixed bin number" or
"Lloyd-Max, minimum mean squared" algorithms defined above, with #
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

to 0.99

.. raw:: latex

   \multicolumn{3}{r}{\textit{continued on next page}}

.. raw:: latex

   \endfoot

.. raw:: latex

   \bottomrule

.. raw:: latex

   \endlastfoot

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
     -  **PVMT**
   * -  :math:`\delta`-:math:`2`:# 
     -  Euclidean (:math:`\ell_{2}`) norm with  distance # 
     -  **G9EV**
   * -  :math:`\delta`-:math:`1`:# 
     -  Manhattan (:math:`\ell_{1}`) norm with  distance # 
     -  **LIFZ**
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
     -  **PVMT**
   * -  :math:`\delta`-:math:`2`:# 
     -  Euclidean (:math:`\ell_{2}`) norm with  distance # 
     -  **G9EV**
   * -  :math:`\delta`-:math:`1`:# 
     -  Manhattan (:math:`\ell_{1}`) norm with  distance # 
     -  **LIFZ**
   * -  :math:`\delta`:#, :math:`\delta`-:math:`\infty`:# 
     -  Chebyshev  (:math:`\ell_{\infty}`) norm with distance (default) # 
     -  **PVMT**
   * -  :math:`\delta`-:math:`2`:# 
     -  Euclidean (:math:`\ell_{2}`) norm with  distance # 
     -  **G9EV**
   * -  :math:`\delta`-:math:`1`:# 
     -  Manhattan (:math:`\ell_{1}`) norm with  distance # 
     -  **LIFZ**
   * -  :math:`l`-:math:`\infty`:# 
     -  Chebyshev (:math:`\ell_{\infty}`) norm 
     -   **PVMT**
   * -  :math:`l`-:math:`2`:# 
     -  Euclidean (:math:`\ell_{2}`) norm 
     -  **G9EV**
   * -  –, :math:`l`-:math:`1`:# 
     -  Manhattan (:math:`\ell_{1}`) norm (default)  
     -  **LIFZ**
   * -  :math:`\delta`:#, :math:`\delta`-:math:`\infty`:# 
     -  Chebyshev  (:math:`\ell_{\infty}`) norm with distance # (default) 
     -  **PVMT**
   * -  :math:`\delta`-:math:`2`:# 
     -  Euclidean (:math:`\ell_{2}`) norm with  distance # 
     -  **G9EV**
   * -  :math:`\delta`-:math:`1`:# 
     -  Manhattan (:math:`\ell_{1}`) norm with  distance # 
     -  **LIFZ**
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
     -  **PVMT**
   * -  :math:`\delta`-:math:`2`:# 
     -  Euclidean (:math:`\ell_{2}`) norm with  distance # 
     -  **G9EV**
   * -  :math:`\delta`-:math:`1`:# 
     -  Manhattan (:math:`\ell_{1}`) norm with  distance # 
     -  **LIFZ**
   * -  –, w:1 
     -  no weighting (default) 
     - 
   * -  w:f 
     -  weighting with function :math:`f` 
     - 

In the above table, # represents numbers.

.. raw:: latex

   \newpage

.. _chap_benchmark sets:
