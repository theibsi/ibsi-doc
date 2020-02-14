.. _chap_report_guidelines:

Radiomics reporting guidelines and nomenclature
===============================================

Reliable and complete reporting is necessary to ensure reproducibility
and validation of results. To help provide a complete report on image
processing and image biomarker extraction, we present the guidelines
below, as well as a nomenclature system to uniquely features.

.. _sec_reporting_guidelines:

Reporting guidelines
--------------------

These guidelines are partially based on the work of
:cite:`Sollini2017N,Lambin2017,Sanduleanu2018iu,Traverso2018yr`.
Additionally, guidelines are derived from the image processing and
feature calculation steps described within this document. An earlier
version was reported elsewhere
:cite:`vallieres2017responsible`.


Patient
^^^^^^^

.. table::
   :widths: 30 20 10 85

   +-----------------+-----------------+-----------------+-----------------+
   | **Topic**       | **Modality**    | **Item**        | **Description** |
   +-----------------+-----------------+-----------------+-----------------+
   | Region of       |                 | 1               | Describe the    |
   | interest [1]_   |                 |                 | region of       |
   |                 |                 |                 | interest that   |
   |                 |                 |                 | is being        |
   |                 |                 |                 | imaged.         |
   +-----------------+-----------------+-----------------+-----------------+
   | Patient         |                 | 2a              | Describe        |
   | preparation     |                 |                 | specific        |
   |                 |                 |                 | instructions    |
   |                 |                 |                 | given to        |
   |                 |                 |                 | patients prior  |
   |                 |                 |                 | to image        |
   |                 |                 |                 | acquisition,    |
   |                 |                 |                 | e.g. fasting    |
   |                 |                 |                 | prior to        |
   |                 |                 |                 | imaging.        |
   +-----------------+-----------------+-----------------+-----------------+
   |                 |                 | 2b              | Describe        |
   |                 |                 |                 | administration  |
   |                 |                 |                 | of drugs to the |
   |                 |                 |                 | patient prior   |
   |                 |                 |                 | to image        |
   |                 |                 |                 | acquisition,    |
   |                 |                 |                 | e.g. muscle     |
   |                 |                 |                 | relaxants.      |
   +-----------------+-----------------+-----------------+-----------------+
   |                 |                 | 2c              | Describe the    |
   |                 |                 |                 | use of specific |
   |                 |                 |                 | equipment for   |
   |                 |                 |                 | patient comfort |
   |                 |                 |                 | during          |
   |                 |                 |                 | scanning, e.g.  |
   |                 |                 |                 | ear plugs.      |
   +-----------------+-----------------+-----------------+-----------------+
   | Radioactive     | PET, SPECT      | 3a              | Describe which  |
   | tracer          |                 |                 | radioactive     |
   |                 |                 |                 | tracer was      |
   |                 |                 |                 | administered to |
   |                 |                 |                 | the patient,    |
   |                 |                 |                 | e.g. 18F-FDG.   |
   +-----------------+-----------------+-----------------+-----------------+
   |                 | PET, SPECT      | 3b              | Describe the    |
   |                 |                 |                 | administration  |
   |                 |                 |                 | method.         |
   +-----------------+-----------------+-----------------+-----------------+
   |                 | PET, SPECT      | 3c              | Describe the    |
   |                 |                 |                 | injected        |
   |                 |                 |                 | activity of the |
   |                 |                 |                 | radioactive     |
   |                 |                 |                 | tracer at       |
   |                 |                 |                 | administration. |
   +-----------------+-----------------+-----------------+-----------------+
   |                 | PET, SPECT      | 3d              | Describe the    |
   |                 |                 |                 | uptake time     |
   |                 |                 |                 | prior to image  |
   |                 |                 |                 | acquisition.    |
   +-----------------+-----------------+-----------------+-----------------+
   |                 | PET, SPECT      | 3e              | Describe how    |
   |                 |                 |                 | competing       |
   |                 |                 |                 | substance       |
   |                 |                 |                 | levels were     |
   |                 |                 |                 | controlled.     |
   |                 |                 |                 | [2]_            |
   +-----------------+-----------------+-----------------+-----------------+
   | Contrast agent  |                 | 4a              | Describe which  |
   |                 |                 |                 | contrast agent  |
   |                 |                 |                 | was             |
   |                 |                 |                 | administered to |
   |                 |                 |                 | the patient.    |
   +-----------------+-----------------+-----------------+-----------------+
   |                 |                 | 4b              | Describe the    |
   |                 |                 |                 | administration  |
   |                 |                 |                 | method.         |
   +-----------------+-----------------+-----------------+-----------------+
   |                 |                 | 4c              | Describe the    |
   |                 |                 |                 | injected        |
   |                 |                 |                 | quantity of     |
   |                 |                 |                 | contrast agent. |
   +-----------------+-----------------+-----------------+-----------------+
   |                 |                 | 4d              | Describe the    |
   |                 |                 |                 | uptake time     |
   |                 |                 |                 | prior to image  |
   |                 |                 |                 | acquisition.    |
   +-----------------+-----------------+-----------------+-----------------+
   |                 |                 | 4e              | Describe how    |
   |                 |                 |                 | competing       |
   |                 |                 |                 | substance       |
   |                 |                 |                 | levels were     |
   |                 |                 |                 | controlled.     |
   +-----------------+-----------------+-----------------+-----------------+
   | Comorbidities   |                 | 5               | Describe if the |
   |                 |                 |                 | patients have   |
   |                 |                 |                 | comorbidities   |
   |                 |                 |                 | that affect     |
   |                 |                 |                 | imaging. [3]_   |
   +-----------------+-----------------+-----------------+-----------------+

Acquisition [4]_
^^^^^^^^^^^^^^^^

.. table::
   :widths: 30 20 10 85

   +-----------------+-----------------+-----------------+-----------------+
   | **Topic**       | **Modality**    | **Item**        | **Description** |
   +-----------------+-----------------+-----------------+-----------------+
   | Acquisition     |                 | 6               | Describe        |
   | protocol        |                 |                 | whether a       |
   |                 |                 |                 | standard        |
   |                 |                 |                 | imaging         |
   |                 |                 |                 | protocol was    |
   |                 |                 |                 | used, and where |
   |                 |                 |                 | its description |
   |                 |                 |                 | may be found.   |
   +-----------------+-----------------+-----------------+-----------------+
   | Scanner type    |                 | 7               | Describe the    |
   |                 |                 |                 | scanner type(s) |
   |                 |                 |                 | and vendor(s)   |
   |                 |                 |                 | used in the     |
   |                 |                 |                 | study.          |
   +-----------------+-----------------+-----------------+-----------------+
   | Imaging         |                 | 8               | Clearly state   |
   | modality        |                 |                 | the imaging     |
   |                 |                 |                 | modality that   |
   |                 |                 |                 | was used in the |
   |                 |                 |                 | study, e.g. CT, |
   |                 |                 |                 | MRI.            |
   +-----------------+-----------------+-----------------+-----------------+
   | Static/dynamic  |                 | 9a              | State if the    |
   | scans           |                 |                 | scans were      |
   |                 |                 |                 | static or       |
   |                 |                 |                 | dynamic.        |
   +-----------------+-----------------+-----------------+-----------------+
   |                 | Dynamic scans   | 9b              | Describe the    |
   |                 |                 |                 | acquisition     |
   |                 |                 |                 | time per time   |
   |                 |                 |                 | frame.          |
   +-----------------+-----------------+-----------------+-----------------+
   |                 | Dynamic scans   | 9c              | Describe any    |
   |                 |                 |                 | temporal        |
   |                 |                 |                 | modelling       |
   |                 |                 |                 | technique that  |
   |                 |                 |                 | was used.       |
   +-----------------+-----------------+-----------------+-----------------+
   | Scanner         |                 | 10              | Describe how    |
   | calibration     |                 |                 | and when the    |
   |                 |                 |                 | scanner was     |
   |                 |                 |                 | calibrated.     |
   +-----------------+-----------------+-----------------+-----------------+
   | Patient         |                 | 11              | Describe        |
   | instructions    |                 |                 | specific        |
   |                 |                 |                 | instructions    |
   |                 |                 |                 | given to the    |
   |                 |                 |                 | patient during  |
   |                 |                 |                 | acquisition,    |
   |                 |                 |                 | e.g. breath     |
   |                 |                 |                 | holding.        |
   +-----------------+-----------------+-----------------+-----------------+
   | Anatomical      |                 | 12              | Describe the    |
   | motion          |                 |                 | method used to  |
   | correction      |                 |                 | minimise the    |
   |                 |                 |                 | effect of       |
   |                 |                 |                 | anatomical      |
   |                 |                 |                 | motion.         |
   +-----------------+-----------------+-----------------+-----------------+
   | Scan duration   |                 | 13              | Describe the    |
   |                 |                 |                 | duration of the |
   |                 |                 |                 | complete scan   |
   |                 |                 |                 | or the time per |
   |                 |                 |                 | bed position.   |
   +-----------------+-----------------+-----------------+-----------------+
   | Tube voltage    | CT              | 14              | Describe the    |
   |                 |                 |                 | peak kilo       |
   |                 |                 |                 | voltage output  |
   |                 |                 |                 | of the X-ray    |
   |                 |                 |                 | source.         |
   +-----------------+-----------------+-----------------+-----------------+
   | Tube current    | CT              | 15              | Describe the    |
   |                 |                 |                 | tube current in |
   |                 |                 |                 | mA.             |
   +-----------------+-----------------+-----------------+-----------------+
   | Time-of-flight  | PET             | 16              | State if        |
   |                 |                 |                 | scanner         |
   |                 |                 |                 | time-of-flight  |
   |                 |                 |                 | capabilities    |
   |                 |                 |                 | are used during |
   |                 |                 |                 | acquisition.    |
   +-----------------+-----------------+-----------------+-----------------+
   | RF coil         | MRI             | 17              | Describe what   |
   |                 |                 |                 | kind RF coil    |
   |                 |                 |                 | used for        |
   |                 |                 |                 | acquisition,    |
   |                 |                 |                 | incl. vendor.   |
   +-----------------+-----------------+-----------------+-----------------+
   | Scanning        | MRI             | 18a             | Describe which  |
   | sequence        |                 |                 | scanning        |
   |                 |                 |                 | sequence was    |
   |                 |                 |                 | acquired.       |
   +-----------------+-----------------+-----------------+-----------------+
   |                 | MRI             | 18b             | Describe which  |
   |                 |                 |                 | sequence        |
   |                 |                 |                 | variant was     |
   |                 |                 |                 | acquired.       |
   +-----------------+-----------------+-----------------+-----------------+
   |                 | MRI             | 18c             | Describe which  |
   |                 |                 |                 | scan options    |
   |                 |                 |                 | apply to the    |
   |                 |                 |                 | current         |
   |                 |                 |                 | sequence, e.g.  |
   |                 |                 |                 | flow            |
   |                 |                 |                 | compensation,   |
   |                 |                 |                 | cardiac gating. |
   +-----------------+-----------------+-----------------+-----------------+
   | Repetition time | MRI             | 19              | Describe the    |
   |                 |                 |                 | time in ms      |
   |                 |                 |                 | between         |
   |                 |                 |                 | subsequent      |
   |                 |                 |                 | pulse           |
   |                 |                 |                 | sequences.      |
   +-----------------+-----------------+-----------------+-----------------+
   | Echo time       | MRI             | 20              | Describe the    |
   |                 |                 |                 | echo time in    |
   |                 |                 |                 | ms.             |
   +-----------------+-----------------+-----------------+-----------------+
   | Echo train      | MRI             | 21              | Describe the    |
   | length          |                 |                 | number of lines |
   |                 |                 |                 | in k-space that |
   |                 |                 |                 | are acquired    |
   |                 |                 |                 | per excitation  |
   |                 |                 |                 | pulse.          |
   +-----------------+-----------------+-----------------+-----------------+
   | Inversion time  | MRI             | 22              | Describe the    |
   |                 |                 |                 | time in ms      |
   |                 |                 |                 | between the     |
   |                 |                 |                 | middle of the   |
   |                 |                 |                 | inverting RF    |
   |                 |                 |                 | pulse to the    |
   |                 |                 |                 | middle of the   |
   |                 |                 |                 | excitation      |
   |                 |                 |                 | pulse.          |
   +-----------------+-----------------+-----------------+-----------------+
   | Flip angle      | MRI             | 23              | Describe the    |
   |                 |                 |                 | flip angle      |
   |                 |                 |                 | produced by the |
   |                 |                 |                 | RF pulses.      |
   +-----------------+-----------------+-----------------+-----------------+
   | Acquisition     | MRI             | 24              | Describe the    |
   | type            |                 |                 | acquisition     |
   |                 |                 |                 | type of the MRI |
   |                 |                 |                 | scan, e.g. 3D.  |
   +-----------------+-----------------+-----------------+-----------------+
   | k-space         | MRI             | 25              | Describe the    |
   | traversal       |                 |                 | acquisition     |
   |                 |                 |                 | trajectory of   |
   |                 |                 |                 | the k-space.    |
   +-----------------+-----------------+-----------------+-----------------+
   | Number of       | MRI             | 26              | Describe the    |
   | averages/       |                 |                 | number of times |
   | excitations     |                 |                 | each point in   |
   |                 |                 |                 | k-space is      |
   |                 |                 |                 | sampled.        |
   +-----------------+-----------------+-----------------+-----------------+
   | Magnetic field  | MRI             | 27              | Describe the    |
   | strength        |                 |                 | nominal         |
   |                 |                 |                 | strength of the |
   |                 |                 |                 | MR magnetic     |
   |                 |                 |                 | field.          |
   +-----------------+-----------------+-----------------+-----------------+

Reconstruction [5]_
^^^^^^^^^^^^^^^^^^^

.. table::
   :widths: 30 20 10 85

   +-----------------+-----------------+-----------------+-----------------+
   | **Topic**       | **Modality**    | **Item**        | **Description** |
   +-----------------+-----------------+-----------------+-----------------+
   | In-plane        |                 | 28              | Describe the    |
   | resolution      |                 |                 | distance        |
   |                 |                 |                 | between pixels, |
   |                 |                 |                 | or              |
   |                 |                 |                 | alternatively   |
   |                 |                 |                 | the field of    |
   |                 |                 |                 | view and matrix |
   |                 |                 |                 | size.           |
   +-----------------+-----------------+-----------------+-----------------+
   | Image slice     |                 | 29              | Describe the    |
   | thickness       |                 |                 | slice           |
   |                 |                 |                 | thickness.      |
   +-----------------+-----------------+-----------------+-----------------+
   | Image slice     |                 | 30              | Describe the    |
   | spacing         |                 |                 | distance        |
   |                 |                 |                 | between image   |
   |                 |                 |                 | slices. [6]_    |
   +-----------------+-----------------+-----------------+-----------------+
   | Convolution     | CT              | 31a             | Describe the    |
   | kernel          |                 |                 | convolution     |
   |                 |                 |                 | kernel used to  |
   |                 |                 |                 | reconstruct the |
   |                 |                 |                 | image.          |
   +-----------------+-----------------+-----------------+-----------------+
   |                 | CT              | 31b             | Describe        |
   |                 |                 |                 | settings        |
   |                 |                 |                 | pertaining to   |
   |                 |                 |                 | iterative       |
   |                 |                 |                 | reconstruction  |
   |                 |                 |                 | algorithms.     |
   +-----------------+-----------------+-----------------+-----------------+
   | Exposure        | CT              | 31c             | Describe the    |
   |                 |                 |                 | exposure (in    |
   |                 |                 |                 | mAs) in slices  |
   |                 |                 |                 | containing the  |
   |                 |                 |                 | region of       |
   |                 |                 |                 | interest.       |
   +-----------------+-----------------+-----------------+-----------------+
   | Reconstruction  | PET             | 32a             | Describe which  |
   | method          |                 |                 | reconstruction  |
   |                 |                 |                 | method was      |
   |                 |                 |                 | used, e.g. 3D   |
   |                 |                 |                 | OSEM.           |
   +-----------------+-----------------+-----------------+-----------------+
   |                 | PET             | 32b             | Describe the    |
   |                 |                 |                 | number of       |
   |                 |                 |                 | iterations for  |
   |                 |                 |                 | iterative       |
   |                 |                 |                 | reconstruction. |
   +-----------------+-----------------+-----------------+-----------------+
   |                 | PET             | 32c             | Describe the    |
   |                 |                 |                 | number of       |
   |                 |                 |                 | subsets for     |
   |                 |                 |                 | iterative       |
   |                 |                 |                 | reconstruction. |
   +-----------------+-----------------+-----------------+-----------------+
   | Point spread    | PET             | 33              | Describe if and |
   | function        |                 |                 | how             |
   | modelling       |                 |                 | point-spread    |
   |                 |                 |                 | function        |
   |                 |                 |                 | modelling was   |
   |                 |                 |                 | performed.      |
   +-----------------+-----------------+-----------------+-----------------+
   | Image           | PET             | 34a             | Describe if and |
   | corrections     |                 |                 | how attenuation |
   |                 |                 |                 | correction was  |
   |                 |                 |                 | performed.      |
   +-----------------+-----------------+-----------------+-----------------+
   |                 | PET             | 34b             | Describe if and |
   |                 |                 |                 | how other forms |
   |                 |                 |                 | of correction   |
   |                 |                 |                 | were performed, |
   |                 |                 |                 | e.g. scatter    |
   |                 |                 |                 | correction,     |
   |                 |                 |                 | randoms         |
   |                 |                 |                 | correction,     |
   |                 |                 |                 | dead time       |
   |                 |                 |                 | correction etc. |
   +-----------------+-----------------+-----------------+-----------------+
   | Reconstruction  | MRI             | 35a             | Describe the    |
   | method          |                 |                 | reconstruction  |
   |                 |                 |                 | method used to  |
   |                 |                 |                 | reconstruct the |
   |                 |                 |                 | image from the  |
   |                 |                 |                 | k-space         |
   |                 |                 |                 | information.    |
   +-----------------+-----------------+-----------------+-----------------+
   |                 | MRI             | 35b             | Describe any    |
   |                 |                 |                 | artifact        |
   |                 |                 |                 | suppression     |
   |                 |                 |                 | methods used    |
   |                 |                 |                 | during          |
   |                 |                 |                 | reconstruction  |
   |                 |                 |                 | to suppress     |
   |                 |                 |                 | artifacts due   |
   |                 |                 |                 | to              |
   |                 |                 |                 | undersampling   |
   |                 |                 |                 | of k-space.     |
   +-----------------+-----------------+-----------------+-----------------+
   | Diffusion-weigh | DWI-MRI         | 36              | Describe the    |
   | ted             |                 |                 | b-values used   |
   | imaging         |                 |                 | for             |
   |                 |                 |                 | diffusion-weigh |
   |                 |                 |                 | ting.           |
   +-----------------+-----------------+-----------------+-----------------+

Image registration
^^^^^^^^^^^^^^^^^^

.. table::
   :widths: 30 20 10 85

   +-----------------+-----------------+-----------------+-----------------+
   | **Topic**       | **Modality**    | **Item**        | **Description** |
   +-----------------+-----------------+-----------------+-----------------+
   | Registration    |                 | 37              | Describe the    |
   | method          |                 |                 | method used to  |
   |                 |                 |                 | register        |
   |                 |                 |                 | multi-modality  |
   |                 |                 |                 | imaging.        |
   +-----------------+-----------------+-----------------+-----------------+

Image processing
^^^^^^^^^^^^^^^^

Data conversion
^^^^^^^^^^^^^^^^

.. table::
   :widths: 30 20 10 85

   +-----------------+-----------------+-----------------+-----------------+
   | **Topic**       | **Modality**    | **Item**        | **Description** |
   +-----------------+-----------------+-----------------+-----------------+
   | SUV             | PET             | 38              | Describe which  |
   | normalisation   |                 |                 | standardised    |
   |                 |                 |                 | uptake value    |
   |                 |                 |                 | (SUV)           |
   |                 |                 |                 | normalisation   |
   |                 |                 |                 | method is used. |
   +-----------------+-----------------+-----------------+-----------------+
   | ADC computation | DWI-MRI         | 39              | Describe how    |
   |                 |                 |                 | apparent        |
   |                 |                 |                 | diffusion       |
   |                 |                 |                 | coefficient     |
   |                 |                 |                 | (ADC) values    |
   |                 |                 |                 | were            |
   |                 |                 |                 | calculated.     |
   +-----------------+-----------------+-----------------+-----------------+
   | Other data      |                 | 40              | Describe any    |
   | conversions     |                 |                 | other           |
   |                 |                 |                 | conversions     |
   |                 |                 |                 | that are        |
   |                 |                 |                 | performed to    |
   |                 |                 |                 | generate e.g.   |
   |                 |                 |                 | perfusion maps. |
   +-----------------+-----------------+-----------------+-----------------+

Post-acquisition processing
^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. table::
   :widths: 30 20 10 85

   +-----------------+-----------------+-----------------+-----------------+
   | **Topic**       | **Modality**    | **Item**        | **Description** |
   +-----------------+-----------------+-----------------+-----------------+
   | Anti-aliasing   |                 | 41              | Describe the    |
   |                 |                 |                 | method used to  |
   |                 |                 |                 | deal with       |
   |                 |                 |                 | anti-aliasing   |
   |                 |                 |                 | when            |
   |                 |                 |                 | down-sampling   |
   |                 |                 |                 | during          |
   |                 |                 |                 | interpolation.  |
   +-----------------+-----------------+-----------------+-----------------+
   | Noise           |                 | 42              | Describe        |
   | suppression     |                 |                 | methods used to |
   |                 |                 |                 | suppress image  |
   |                 |                 |                 | noise.          |
   +-----------------+-----------------+-----------------+-----------------+
   | Post-reconstruc | PET             | 43              | Describe the    |
   | tion            |                 |                 | width of the    |
   | smoothing       |                 |                 | Gaussian filter |
   | filter          |                 |                 | (FWHM) to       |
   |                 |                 |                 | spatially       |
   |                 |                 |                 | smooth          |
   |                 |                 |                 | intensities.    |
   +-----------------+-----------------+-----------------+-----------------+
   | Skull stripping | MRI (brain)     | 44              | Describe method |
   |                 |                 |                 | used to perform |
   |                 |                 |                 | skull           |
   |                 |                 |                 | stripping.      |
   +-----------------+-----------------+-----------------+-----------------+
   | Non-uniformity  | MRI             | 45              | Describe the    |
   | correction [7]_ |                 |                 | method and      |
   |                 |                 |                 | settings used   |
   |                 |                 |                 | to perform      |
   |                 |                 |                 | non-uniformity  |
   |                 |                 |                 | correction.     |
   +-----------------+-----------------+-----------------+-----------------+
   | Intensity       |                 | 46              | Describe the    |
   | normalisation   |                 |                 | method and      |
   |                 |                 |                 | settings used   |
   |                 |                 |                 | to normalise    |
   |                 |                 |                 | intensity       |
   |                 |                 |                 | distributions   |
   |                 |                 |                 | within a        |
   |                 |                 |                 | patient or      |
   |                 |                 |                 | patient cohort. |
   +-----------------+-----------------+-----------------+-----------------+
   | Other           |                 | 47              | Describe any    |
   | post-acquisitio |                 |                 | other methods   |
   | n               |                 |                 | that were used  |
   | processing      |                 |                 | to process the  |
   | methods         |                 |                 | image and are   |
   |                 |                 |                 | not mentioned   |
   |                 |                 |                 | separately in   |
   |                 |                 |                 | this list.      |
   +-----------------+-----------------+-----------------+-----------------+

Segmentation
^^^^^^^^^^^^

.. table::
   :widths: 30 20 10 85

   +-----------------+-----------------+-----------------+-----------------+
   | **Topic**       | **Modality**    | **Item**        | **Description** |
   +-----------------+-----------------+-----------------+-----------------+
   | Segmentation    |                 | 48a             | Describe how    |
   | method          |                 |                 | regions of      |
   |                 |                 |                 | interest were   |
   |                 |                 |                 | segmented, e.g. |
   |                 |                 |                 | manually.       |
   +-----------------+-----------------+-----------------+-----------------+
   |                 |                 | 48b             | Describe the    |
   |                 |                 |                 | number of       |
   |                 |                 |                 | experts, their  |
   |                 |                 |                 | expertise and   |
   |                 |                 |                 | consensus       |
   |                 |                 |                 | strategies for  |
   |                 |                 |                 | manual          |
   |                 |                 |                 | delineation.    |
   +-----------------+-----------------+-----------------+-----------------+
   |                 |                 | 48c             | Describe        |
   |                 |                 |                 | methods and     |
   |                 |                 |                 | settings used   |
   |                 |                 |                 | for             |
   |                 |                 |                 | semi-automatic  |
   |                 |                 |                 | and fully       |
   |                 |                 |                 | automatic       |
   |                 |                 |                 | segmentation.   |
   +-----------------+-----------------+-----------------+-----------------+
   |                 |                 | 48d             | Describe which  |
   |                 |                 |                 | image was used  |
   |                 |                 |                 | to define       |
   |                 |                 |                 | segmentation in |
   |                 |                 |                 | case of         |
   |                 |                 |                 | multi-modality  |
   |                 |                 |                 | imaging.        |
   +-----------------+-----------------+-----------------+-----------------+
   | Conversion to   |                 | 49              | Describe the    |
   | mask            |                 |                 | method used to  |
   |                 |                 |                 | convert         |
   |                 |                 |                 | polygonal or    |
   |                 |                 |                 | mesh-based      |
   |                 |                 |                 | segmentations   |
   |                 |                 |                 | to a            |
   |                 |                 |                 | voxel-based     |
   |                 |                 |                 | mask.           |
   +-----------------+-----------------+-----------------+-----------------+

.. _section-1:

Image interpolation
^^^^^^^^^^^^^^^^^^^

.. table::
   :widths: 30 20 10 85

   +-----------------+-----------------+-----------------+-----------------+
   | **Topic**       | **Modality**    | **Item**        | **Description** |
   +-----------------+-----------------+-----------------+-----------------+
   | Interpolation   |                 | 50a             | Describe which  |
   | method          |                 |                 | interpolation   |
   |                 |                 |                 | algorithm was   |
   |                 |                 |                 | used to         |
   |                 |                 |                 | interpolate the |
   |                 |                 |                 | image.          |
   +-----------------+-----------------+-----------------+-----------------+
   |                 |                 | 50b             | Describe how    |
   |                 |                 |                 | the position of |
   |                 |                 |                 | the             |
   |                 |                 |                 | interpolation   |
   |                 |                 |                 | grid was        |
   |                 |                 |                 | defined, e.g.   |
   |                 |                 |                 | align by        |
   |                 |                 |                 | center.         |
   +-----------------+-----------------+-----------------+-----------------+
   |                 |                 | 50c             | Describe how    |
   |                 |                 |                 | the dimensions  |
   |                 |                 |                 | of the          |
   |                 |                 |                 | interpolation   |
   |                 |                 |                 | grid were       |
   |                 |                 |                 | defined, e.g.   |
   |                 |                 |                 | rounded to      |
   |                 |                 |                 | nearest         |
   |                 |                 |                 | integer.        |
   +-----------------+-----------------+-----------------+-----------------+
   |                 |                 | 50d             | Describe how    |
   |                 |                 |                 | extrapolation   |
   |                 |                 |                 | beyond the      |
   |                 |                 |                 | original image  |
   |                 |                 |                 | was handled.    |
   +-----------------+-----------------+-----------------+-----------------+
   | Voxel           |                 | 51              | Describe the    |
   | dimensions      |                 |                 | size of the     |
   |                 |                 |                 | interpolated    |
   |                 |                 |                 | voxels.         |
   +-----------------+-----------------+-----------------+-----------------+
   | Intensity       | CT              | 52              | Describe how    |
   | rounding        |                 |                 | fractional      |
   |                 |                 |                 | Hounsfield      |
   |                 |                 |                 | Units are       |
   |                 |                 |                 | rounded to      |
   |                 |                 |                 | integer values  |
   |                 |                 |                 | after           |
   |                 |                 |                 | interpolation.  |
   +-----------------+-----------------+-----------------+-----------------+

ROI interpolation
^^^^^^^^^^^^^^^^^

.. table::
   :widths: 30 20 10 85

   +-----------------+-----------------+-----------------+-----------------+
   | **Topic**       | **Modality**    | **Item**        | **Description** |
   +-----------------+-----------------+-----------------+-----------------+
   | Interpolation   |                 | 53              | Describe which  |
   | method          |                 |                 | interpolation   |
   |                 |                 |                 | algorithm was   |
   |                 |                 |                 | used to         |
   |                 |                 |                 | interpolate the |
   |                 |                 |                 | region of       |
   |                 |                 |                 | interest mask.  |
   +-----------------+-----------------+-----------------+-----------------+
   | Partially       |                 | 54              | Describe how    |
   | masked voxels   |                 |                 | partially       |
   |                 |                 |                 | masked voxels   |
   |                 |                 |                 | after           |
   |                 |                 |                 | interpolation   |
   |                 |                 |                 | are handled.    |
   +-----------------+-----------------+-----------------+-----------------+

Re-segmentation
^^^^^^^^^^^^^^^

.. table::
   :widths: 30 20 10 85

   +-----------------+-----------------+-----------------+-----------------+
   | **Topic**       | **Modality**    | **Item**        | **Description** |
   +-----------------+-----------------+-----------------+-----------------+
   | Re-segmentation |                 | 55              | Describe which  |
   | methods         |                 |                 | methods and     |
   |                 |                 |                 | settings are    |
   |                 |                 |                 | used to         |
   |                 |                 |                 | re-segment the  |
   |                 |                 |                 | ROI intensity   |
   |                 |                 |                 | mask.           |
   +-----------------+-----------------+-----------------+-----------------+

Discretisation
^^^^^^^^^^^^^^

.. table::
   :widths: 30 20 10 85

   +-----------------+-----------------+-----------------+-----------------+
   | **Topic**       | **Modality**    | **Item**        | **Description** |
   +-----------------+-----------------+-----------------+-----------------+
   | Discretisation  |                 | 56a             | Describe the    |
   | method [8]_     |                 |                 | method used to  |
   |                 |                 |                 | discretise      |
   |                 |                 |                 | image           |
   |                 |                 |                 | intensities.    |
   +-----------------+-----------------+-----------------+-----------------+
   |                 |                 | 56b             | Describe the    |
   |                 |                 |                 | number of bins  |
   |                 |                 |                 | (FBN) or the    |
   |                 |                 |                 | bin size (FBS)  |
   |                 |                 |                 | used for        |
   |                 |                 |                 | discretisation. |
   +-----------------+-----------------+-----------------+-----------------+
   |                 |                 | 56c             | Describe the    |
   |                 |                 |                 | lowest          |
   |                 |                 |                 | intensity in    |
   |                 |                 |                 | the first bin   |
   |                 |                 |                 | for FBS         |
   |                 |                 |                 | discretisation. |
   |                 |                 |                 | [9]_            |
   +-----------------+-----------------+-----------------+-----------------+



Image transformation
^^^^^^^^^^^^^^^^^^^^

.. table::
   :widths: 30 20 10 85

   +-----------------+-----------------+-----------------+-----------------+
   | **Topic**       | **Modality**    | **Item**        | **Description** |
   +-----------------+-----------------+-----------------+-----------------+
   | Image           |                 | 57              | Describe the    |
   | filter [10]_    |                 |                 | methods and     |
   |                 |                 |                 | settings used   |
   |                 |                 |                 | to filter       |
   |                 |                 |                 | images, e.g.    |
   |                 |                 |                 | Laplacian-of-Ga |
   |                 |                 |                 | ussian.         |
   +-----------------+-----------------+-----------------+-----------------+

Image biomarker computation
^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. table::
   :widths: 30 20 10 85

   +-----------------+-----------------+-----------------+-----------------+
   | **Topic**       | **Modality**    | **Item**        | **Description** |
   +-----------------+-----------------+-----------------+-----------------+
   | Biomarker set   |                 | 58              | Describe which  |
   |                 |                 |                 | set of image    |
   |                 |                 |                 | biomarkers is   |
   |                 |                 |                 | computed and    |
   |                 |                 |                 | refer to their  |
   |                 |                 |                 | definitions or  |
   |                 |                 |                 | provide these.  |
   +-----------------+-----------------+-----------------+-----------------+
   | IBSI compliance |                 | 59              | State if the    |
   |                 |                 |                 | software used   |
   |                 |                 |                 | to extract the  |
   |                 |                 |                 | set of image    |
   |                 |                 |                 | biomarkers is   |
   |                 |                 |                 | compliant with  |
   |                 |                 |                 | the IBSI        |
   |                 |                 |                 | benchmarks.     |
   |                 |                 |                 | [11]_           |
   +-----------------+-----------------+-----------------+-----------------+
   | Robustness      |                 | 60              | Describe how    |
   |                 |                 |                 | robustness of   |
   |                 |                 |                 | the image       |
   |                 |                 |                 | biomarkers was  |
   |                 |                 |                 | assessed, e.g.  |
   |                 |                 |                 | test-retest     |
   |                 |                 |                 | analysis.       |
   +-----------------+-----------------+-----------------+-----------------+
   | Software        |                 | 61              | Describe which  |
   | availability    |                 |                 | software and    |
   |                 |                 |                 | version was     |
   |                 |                 |                 | used to compute |
   |                 |                 |                 | image           |
   |                 |                 |                 | biomarkers.     |
   +-----------------+-----------------+-----------------+-----------------+

.. _section-2:

Image biomarker computation - texture parameters
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. table::
   :widths: 30 20 10 85

   +-----------------+-----------------+-----------------+-----------------+
   | **Topic**       | **Modality**    | **Item**        | **Description** |
   +-----------------+-----------------+-----------------+-----------------+
   | Texture matrix  |                 | 62              | Define how      |
   | aggregation     |                 |                 | texture-matrix  |
   |                 |                 |                 | based           |
   |                 |                 |                 | biomarkers were |
   |                 |                 |                 | computed from   |
   |                 |                 |                 | underlying      |
   |                 |                 |                 | texture         |
   |                 |                 |                 | matrices.       |
   +-----------------+-----------------+-----------------+-----------------+
   | Distance        |                 | 63              | Define how CM,  |
   | weighting       |                 |                 | RLM, NGTDM and  |
   |                 |                 |                 | NGLDM weight    |
   |                 |                 |                 | distances, e.g. |
   |                 |                 |                 | no weighting.   |
   +-----------------+-----------------+-----------------+-----------------+
   | CM symmetry     |                 | 64              | Define whether  |
   |                 |                 |                 | symmetric or    |
   |                 |                 |                 | asymmetric      |
   |                 |                 |                 | co-occurrence   |
   |                 |                 |                 | matrices were   |
   |                 |                 |                 | computed.       |
   +-----------------+-----------------+-----------------+-----------------+
   | CM distance     |                 | 65              | Define the      |
   |                 |                 |                 | (Chebyshev)     |
   |                 |                 |                 | distance at     |
   |                 |                 |                 | which           |
   |                 |                 |                 | co-occurrence   |
   |                 |                 |                 | of intensities  |
   |                 |                 |                 | is determined,  |
   |                 |                 |                 | e.g. 1.         |
   +-----------------+-----------------+-----------------+-----------------+
   | SZM linkage     |                 | 66              | Define the      |
   | distance        |                 |                 | distance and    |
   |                 |                 |                 | distance norm   |
   |                 |                 |                 | for which       |
   |                 |                 |                 | voxels with the |
   |                 |                 |                 | same intensity  |
   |                 |                 |                 | are considered  |
   |                 |                 |                 | to belong to    |
   |                 |                 |                 | the same zone   |
   |                 |                 |                 | for the purpose |
   |                 |                 |                 | of constructing |
   |                 |                 |                 | an SZM, e.g.    |
   |                 |                 |                 | Chebyshev       |
   |                 |                 |                 | distance of 1.  |
   +-----------------+-----------------+-----------------+-----------------+
   | DZM linkage     |                 | 67              | Define the      |
   | distance        |                 |                 | distance and    |
   |                 |                 |                 | distance norm   |
   |                 |                 |                 | for which       |
   |                 |                 |                 | voxels with the |
   |                 |                 |                 | same intensity  |
   |                 |                 |                 | are considered  |
   |                 |                 |                 | to belong to    |
   |                 |                 |                 | the same zone   |
   |                 |                 |                 | for the purpose |
   |                 |                 |                 | of constructing |
   |                 |                 |                 | a DZM, e.g.     |
   |                 |                 |                 | Chebyshev       |
   |                 |                 |                 | distance of 1.  |
   +-----------------+-----------------+-----------------+-----------------+
   | DZM zone        |                 | 68              | Define the      |
   | distance norm   |                 |                 | distance norm   |
   |                 |                 |                 | for determining |
   |                 |                 |                 | the distance of |
   |                 |                 |                 | zones to the    |
   |                 |                 |                 | border of the   |
   |                 |                 |                 | ROI, e.g.       |
   |                 |                 |                 | Manhattan       |
   |                 |                 |                 | distance.       |
   +-----------------+-----------------+-----------------+-----------------+
   | NGTDM distance  |                 | 69              | Define the      |
   |                 |                 |                 | neighbourhood   |
   |                 |                 |                 | distance and    |
   |                 |                 |                 | distance norm   |
   |                 |                 |                 | for the NGTDM,  |
   |                 |                 |                 | e.g. Chebyshev  |
   |                 |                 |                 | distance of 1.  |
   +-----------------+-----------------+-----------------+-----------------+
   | NGLDM distance  |                 | 70              | Define the      |
   |                 |                 |                 | neighbourhood   |
   |                 |                 |                 | distance and    |
   |                 |                 |                 | distance norm   |
   |                 |                 |                 | for the NGLDM,  |
   |                 |                 |                 | e.g. Chebyshev  |
   |                 |                 |                 | distance of 1.  |
   +-----------------+-----------------+-----------------+-----------------+
   | NGLDM           |                 | 71              | Define the      |
   | coarseness      |                 |                 | coarseness      |
   |                 |                 |                 | parameter for   |
   |                 |                 |                 | the NGLDM, e.g. |
   |                 |                 |                 | 0.              |
   +-----------------+-----------------+-----------------+-----------------+

Machine learning and radiomics analysis
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. table::
   :widths: 30 20 10 85

   +-----------------+-----------------+-----------------+-----------------+
   | **Topic**       | **Modality**    | **Item**        | **Description** |
   +-----------------+-----------------+-----------------+-----------------+
   | Diagnostic and  |                 | 72              | See the TRIPOD  |
   | prognostic      |                 |                 | guidelines for  |
   | modelling       |                 |                 | reporting on    |
   |                 |                 |                 | diagnostic and  |
   |                 |                 |                 | prognostic      |
   |                 |                 |                 | modelling.      |
   +-----------------+-----------------+-----------------+-----------------+
   | Comparison with |                 | 73              | Describe where  |
   | known factors   |                 |                 | performance of  |
   |                 |                 |                 | radiomics       |
   |                 |                 |                 | models is       |
   |                 |                 |                 | compared with   |
   |                 |                 |                 | known           |
   |                 |                 |                 | (clinical)      |
   |                 |                 |                 | factors.        |
   +-----------------+-----------------+-----------------+-----------------+
   | Multicollineari |                 | 74              | Describe where  |
   | ty              |                 |                 | the             |
   |                 |                 |                 | multicollineari |
   |                 |                 |                 | ty              |
   |                 |                 |                 | between image   |
   |                 |                 |                 | biomarkers in   |
   |                 |                 |                 | the signature   |
   |                 |                 |                 | is assessed.    |
   +-----------------+-----------------+-----------------+-----------------+
   | Model           |                 | 75              | Describe where  |
   | availability    |                 |                 | radiomics       |
   |                 |                 |                 | models with the |
   |                 |                 |                 | necessary       |
   |                 |                 |                 | pre-processing  |
   |                 |                 |                 | information may |
   |                 |                 |                 | be found.       |
   +-----------------+-----------------+-----------------+-----------------+
   | Data            |                 | 76              | Describe where  |
   | availability    |                 |                 | imaging data    |
   |                 |                 |                 | and relevant    |
   |                 |                 |                 | meta-data used  |
   |                 |                 |                 | in the study    |
   |                 |                 |                 | may be found.   |
   +-----------------+-----------------+-----------------+-----------------+


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

The following is a list of the feature families in this document and
their suggested abbreviations:


+-------------------------------------------+------------------+--------+
| **feature family**                        | **abbreviation** |        |
+===========================================+==================+========+
| morphology                                | MORPH            | *HCUG* |
+-------------------------------------------+------------------+--------+
| local intensity                           | LI               | *9ST6* |
+-------------------------------------------+------------------+--------+
| intensity-based statistics                | IS, STAT         | *UHIW* |
+-------------------------------------------+------------------+--------+
| intensity histogram                       | IH               | *ZVCW* |
+-------------------------------------------+------------------+--------+
| intensity-volume histogram                | IVH              | *P88C* |
+-------------------------------------------+------------------+--------+
| grey level co-occurrence matrix           | GLCM, CM         | *LFYI* |
+-------------------------------------------+------------------+--------+
| grey level run length matrix              | GLRLM, RLM       | *TP0I* |
+-------------------------------------------+------------------+--------+
| grey level size zone matrix               | GLSZM, SZM       | *9SAK* |
+-------------------------------------------+------------------+--------+
| grey level distance zone matrix           | GLDZM, DZM       | *VMDZ* |
+-------------------------------------------+------------------+--------+
| neighbourhood grey tone difference matrix | NGTDM            | *IPET* |
+-------------------------------------------+------------------+--------+
| neighbouring grey level dependence matrix | NGLDM            | *REK0* |
+-------------------------------------------+------------------+--------+


Abbreviating feature aggregation
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The following is a list of feature families and the possible aggregation
methods:

.. table::
   :widths: 30 80 10

   +----+-------------------------------+--------+
   |    | **morphology, LI**            |        |
   +====+===============================+========+
   | -, | features are 3D by definition | *DHQ4* |
   +----+-------------------------------+--------+


.. table::
   :widths: 30 80 10

   +------+--------------------------------------+--------+
   |      | **IS, IH, IVH**                      |        |
   +======+======================================+========+
   | 2D   | averaged over slices (rare)          | *3IDG* |
   +------+--------------------------------------+--------+
   | -,3D | calculated over the volume (default) | *DHQ4* |
   +------+--------------------------------------+--------+


.. table::
   :widths: 30 80 10

   +---------------------+------------------------------------------+--------+
   |                     | **GLCM, GLRLM**                          |        |
   +=====================+==========================================+========+
   | 2D:avg              | averaged over slices and directions      | *BTW3* |
   +---------------------+------------------------------------------+--------+
   | 2D:mrg, 2Dsmrg      | merged directions per slice and averaged | *SUJT* |
   +---------------------+------------------------------------------+--------+
   | 2.5D:avg, 2.5D:dmrg | merged per direction and averaged        | *JJUI* |
   +---------------------+------------------------------------------+--------+
   | 2.5D:mrg, 2.5D:vmrg | merged over all slices                   | *ZW7Z* |
   +---------------------+------------------------------------------+--------+
   | 3D:avg              | averaged over 3D directions              | *ITBB* |
   +---------------------+------------------------------------------+--------+
   | 3D:mrg              | merged 3D directions                     | *IAZD* |
   +---------------------+------------------------------------------+--------+

.. table::
   :widths: 30 80 10

   +------+----------------------------------+--------+
   |      | **GLSZM, GLDZM, NGTDM, NGLDM**   |        |
   +======+==================================+========+
   | 2D   | averaged over slices             | *8QNN* |
   +------+----------------------------------+--------+
   | 2.5D | merged over all slices           | *62GR* |
   +------+----------------------------------+--------+
   | 3D   | calculated from single 3D matrix | *KOBO* |
   +------+----------------------------------+--------+


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


+---------------------------------+------------------------------+
| **interpolation method**        | **notation**                 |
+=================================+==============================+
| none                            | INT:–                        |
+---------------------------------+------------------------------+
| nearest neighbour interpolation | NNB:\ *dim*:#                |
+---------------------------------+------------------------------+
| linear interpolation            | LIN:\ *dim*:#                |
+---------------------------------+------------------------------+
| cubic convolution interpolation | CCI:\ *dim*:#                |
+---------------------------------+------------------------------+
| cubic spline interpolation      | CSI:\ *dim*:#, SI3:\ *dim*:# |
+---------------------------------+------------------------------+


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


+----------------------------+----------------------+--------+
| **re-segmentation method** | **notation**         |        |
+============================+======================+========+
| none                       | RS:–                 |        |
+----------------------------+----------------------+--------+
| range                      | RS:[#,#]             | *USB3* |
+----------------------------+----------------------+--------+
| outlier filtering          | RS:#\ :math:`\sigma` | *7ACA* |
+----------------------------+----------------------+--------+


In the table above # signify numbers. A re-segmentation range can be
half-open, i.e. RS:[#,\ :math:`\infty`). Re-segmentation methods may be
combined, i.e. both range and outlier filtering methods may be used.
This is noted as RS:[#,#]+#\ :math:`\sigma` or
RS:#\ :math:`\sigma`\ +[#,#]. The following are examples of the
application of the above notation:

-  mean\ :sub:`IS, CT, RS:[-200,150]`: intensity statistical *mean*
   feature, based on an ROI in a CT image that was re-segmented within a
   [-200,150] HU range.

-  mean\ :sub:`IS, PET:SUV, RS:[3,\ ∞)`: intensity
   statistical *mean* feature, based on an ROI in a PET image with SUV
   values, that was re-segmented to contain only SUV of 3 and above.

-  mean\ :sub:`IS, MRI:T1, RS:3\ σ`: intensity statistical
   *mean* feature, based on an ROI in a T1-weighted MR image where the
   ROI was re-segmented by removing voxels with an intensity outside a
   :math:`\mu \pm 3\sigma` range.

Abbreviating discretisation
^^^^^^^^^^^^^^^^^^^^^^^^^^^

The following is a list of discretisation methods and the suggested
notation. Note that # is the value of the relevant discretisation
parameter, e.g. number of bins or bin size, including units.


+---------------------------------+--------------+--------+
| **discretisation method**       | **notation** |        |
+=================================+==============+========+
| none                            | DIS:–        |        |
+---------------------------------+--------------+--------+
| fixed bin size                  | FBS:#        | *Q3RU* |
+---------------------------------+--------------+--------+
| fixed bin number                | FBN:#        | *K15C* |
+---------------------------------+--------------+--------+
| histogram equalisation          | EQ:#         |        |
+---------------------------------+--------------+--------+
| Lloyd-Max, minimum mean squared | LM:#, MMS:#  |        |
+---------------------------------+--------------+--------+


In the table above, # signify numbers such as the number of bins or
their width. Histogram equalisation of the ROI intensities can be
performed before the "none", "fixed bin size", "fixed bin number" or
"Lloyd-Max, minimum mean squared" algorithms defined above, with #
specifying the number of bins in the histogram to be equalised. The
following are examples of the application of the above notation:

-  mean\ :sub:`IH,PET:SUV,RS[0,∞],FBS:0.2`: intensity
   histogram *mean* feature, based on an ROI in a SUV-PET image, with
   bin-width of 0.2 SUV, and binning from 0.0 SUV.

-  grey level variance\ :sub:`SZM,MR:T1,RS:3σ,FBN:64`:
   size zone matrix-based *grey level variance* feature, based on an ROI
   in a T1-weighted MR image, with :math:`3\sigma` re-segmentation and
   subsequent binning into 64 bins.


Abbreviating feature-specific parameters
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Some features and feature families require additional parameters, which
may be varied. These are the following:


.. table::
   :widths: 55 130 10
   :align: center

   +------------+----------------------------------------------------------------------+--------+
   |            | **GLCM**                                                             |        |
   +============+======================================================================+========+
   |            | *Co-occurrence matrix symmetry*                                      |        |
   +------------+----------------------------------------------------------------------+--------+
   | -, SYM     | symmetrical co-occurrence matrices                                   |        |
   +------------+----------------------------------------------------------------------+--------+
   | ASYM       | asymmetrical co-occurrence matrices (not recommended)                |        |
   +------------+----------------------------------------------------------------------+--------+
   |            | *Distance*                                                           |        |
   +------------+----------------------------------------------------------------------+--------+
   | δ:#, δ-∞:# | Chebyshev (:math:`\ell_{∞}`) norm with distance # (default)          | *PVMT* |
   +------------+----------------------------------------------------------------------+--------+
   | δ-2:#      | Euclidean (:math:`\ell_{2}`) norm with distance #                    | *G9EV* |
   +------------+----------------------------------------------------------------------+--------+
   | δ-1:#      | Manhattan (:math:`\ell_{1}`) norm with distance #                    | *LIFZ* |
   +------------+----------------------------------------------------------------------+--------+
   |            | *Distance Weighting*                                                 |        |
   +------------+----------------------------------------------------------------------+--------+
   | -,w:1      | no weighting (default)                                               |        |
   +------------+----------------------------------------------------------------------+--------+
   | w:f        | weighting with function :math:`f`                                    |        |
   +------------+----------------------------------------------------------------------+--------+


.. table::
   :widths: 55 130 10
   :align: center

   +-------+-------------------------------------+--+
   |       | **GLRLM**                           |  |
   +=======+=====================================+==+
   |       | *distance weighting*                |  |
   +-------+-------------------------------------+--+
   | -,w:1 | no weighting (default)              |  |
   +-------+-------------------------------------+--+
   | w:f   | weighting with function :math:`f`   |  |
   +-------+-------------------------------------+--+


.. table::
   :widths: 55 130 10

   +------------+-------------------------------------------------------------+--------+
   |            | **GLSZM**                                                   |        |
   +============+=============================================================+========+
   |            | *Linkage distance*                                          |        |
   +------------+-------------------------------------------------------------+--------+
   | δ:#, δ-∞:# | Chebyshev (:math:`\ell_{∞}`) norm with distance # (default) | *PVMT* |
   +------------+-------------------------------------------------------------+--------+
   | δ-2:#      | Euclidean (:math:`\ell_{2}`) norm with distance #           | *G9EV* |
   +------------+-------------------------------------------------------------+--------+
   | δ-1:#      | Manhattan (:math:`\ell_{1}`) norm with distance #           | *LIFZ* |
   +------------+-------------------------------------------------------------+--------+


.. table::
   :widths: 55 130 10

   +------------+-------------------------------------------------------------+--------+
   |            | **GLDZM**                                                   |        |
   +============+=============================================================+========+
   |            | *Linkage distance*                                          |        |
   +------------+-------------------------------------------------------------+--------+
   | δ:#, δ-∞:# | Chebyshev (:math:`\ell_{∞}`) norm with distance # (default) | *PVMT* |
   +------------+-------------------------------------------------------------+--------+
   | δ-2:#      | Euclidean (:math:`\ell_{2}`) norm with distance #           | *G9EV* |
   +------------+-------------------------------------------------------------+--------+
   | δ-1:#      | Manhattan (:math:`\ell_{1}`) norm with distance #           | *LIFZ* |
   +------------+-------------------------------------------------------------+--------+
   |            | *zone distance norm*                                        |        |
   +------------+-------------------------------------------------------------+--------+
   | l-∞:#      | Chebyshev (:math:`\ell_{∞}`) norm                           | *PVMT* |
   +------------+-------------------------------------------------------------+--------+
   | l-2:#      | Euclidean (:math:`\ell_{2}`) norm                           | *G9EV* |
   +------------+-------------------------------------------------------------+--------+
   | -,l-1:#    | Manhattan (:math:`\ell_{1}`) norm (default)                 | *LIFZ* |
   +------------+-------------------------------------------------------------+--------+



.. table::
   :widths: 30 80 10


   +------------+-------------------------------------------------------------+--------+
   |            | **NGTDM**                                                   |        |
   +============+=============================================================+========+
   |            | *distance*                                                  |        |
   +------------+-------------------------------------------------------------+--------+
   | δ:#, δ-∞:# | Chebyshev (:math:`\ell_{∞}`) norm with distance # (default) | *PVMT* |
   +------------+-------------------------------------------------------------+--------+
   | δ-2:#      | Euclidean (:math:`\ell_{2}`) norm with distance #           | *G9EV* |
   +------------+-------------------------------------------------------------+--------+
   | δ-1:#      | Manhattan (:math:`\ell_{1}`) norm with distance #           | *LIFZ* |
   +------------+-------------------------------------------------------------+--------+
   |            | *weighting*                                                 |        |
   +------------+-------------------------------------------------------------+--------+
   | -,w:1      | no weighting (default)                                      |        |
   +------------+-------------------------------------------------------------+--------+
   | w:f        | weighting with function f                                   |        |
   +------------+-------------------------------------------------------------+--------+


.. table::
   :widths: 30 80 10

   +------------+-------------------------------------------------------------+--------+
   |            | **NGLDM**                                                   |        |
   +============+=============================================================+========+
   |            | *dependence coarseness*                                     |        |
   +------------+-------------------------------------------------------------+--------+
   | α:#        | dependence coarseness parameter with value #                |        |
   +------------+-------------------------------------------------------------+--------+
   |            | *distance*                                                  |        |
   +------------+-------------------------------------------------------------+--------+
   | δ:#, δ-∞:# | Chebyshev (:math:`\ell_{∞}`) norm with distance # (default) | *PVMT* |
   +------------+-------------------------------------------------------------+--------+
   | δ-2:#      | Euclidean (:math:`\ell_{2}`) norm with distance #           | *G9EV* |
   +------------+-------------------------------------------------------------+--------+
   | δ-1:#      | Manhattan (:math:`\ell_{1}`) norm with distance #           | *LIFZ* |
   +------------+-------------------------------------------------------------+--------+
   |            | *weighting*                                                 |        |
   +------------+-------------------------------------------------------------+--------+
   | -,w:1      | no weighting (default)                                      |        |
   +------------+-------------------------------------------------------------+--------+
   | w:f        | weighting with function :math:`f`                           |        |
   +------------+-------------------------------------------------------------+--------+


In the above tables, # represents numbers.


.. [1]
   Also referred to as volume of interest.

.. [2]
   An example is glucose present in the blood which competes with the
   uptake of 18F-FDG tracer in tumour tissue. To reduce competition with
   the tracer, patients are usually asked to fast for several hours and
   a blood glucose measurement may be conducted prior to tracer
   administration.

.. [3]
   An example of a comorbidity that may affect image quality in 18F-FDG
   PET scans are type I and type II diabetes melitus, as well as kidney
   failure.

.. [4]
   Many acquisition parameters may be extracted from DICOM header
   meta-data, or calculated from them.

.. [5]
   Many reconstruction parameters may be extracted from DICOM header
   meta-data.

.. [6]
   Spacing between image slicing is commonly, but not necessarily, the
   same as the slice thickness.

.. [7]
   Also known as bias-field correction.

.. [8]
   Discretisation may be performed separately to create intensity-volume
   histograms. If this is indeed the case, this should be described as
   well.

.. [9]
   This is typically set by range re-segmentation.

.. [10]
   The IBSI has not introduced image transformation into the
   standardised image processing scheme, and is in the process of
   benchmarking various common filters. This section may therefore be
   expanded in the future.

.. [11]
   A software is compliant if and only if it is able to reproduce the
   image biomarker benchmarks for the digital phantom and for one or
   more image processing configurations using the radiomics CT phantom.
   Reviewers may demand that you provide the IBSI compliance spreadsheet
   for your software.


