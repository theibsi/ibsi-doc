Introduction
============

A biomarker is “*a characteristic that is objectively measured and
evaluated as an indicator of normal biological processes, pathogenic
processes, or pharmacologic responses to a therapeutic
intervention*” \[1_\]. Biomarkers may be
measured from a wide variety of sources, such as tissue samples, cell
plating, and imaging. The latter are often referred to as imaging
biomarkers. Imaging biomarkers consist of both qualitative biomarkers,
which require expert interpretation, and quantitative biomarkers which
are based on mathematical definitions. Calculation of quantitative
imaging biomarkers can be automated, which enables high-throughput
analyses. We refer to such (high-throughput) quantitative biomarkers as
image biomarkers to differentiate them from qualitative imaging
biomarkers. Image biomarkers characterise the contents of (regions of)
an image, such as *volume* or *mean intensity*. Because of the
historically close relationship with the computer vision field, image
biomarkers are also referred to as image features. The term *features*,
instead of biomarkers, will be used throughout the remainder of the
reference manual, as the contents are generally applicable and not
limited to life sciences and medicine only.

This work focuses specifically on the (high-throughput) extraction of
image biomarkers from acquired, reconstructed and stored imaging.
High-throughput quantitative image analysis (radiomics) has shown
considerable growth in e.g. cancer research
\[2_\], but the scarceness of consensus
guidelines and definitions has led to it being described as a “wild
frontier” \[3_\]. This reference manual
therefore presents an effort to chart a course through part of this
frontier by presenting consensus-based recommendations, guidelines,
benchmarks and definitions for image biomarker extraction, and thus
increase the reproducibility of studies involving radiomics.

We opted for a specific focus on image biomarker extraction from
acquired imaging. Thus, imaging biomarker validation, viewed in a
broader framework such as the one presented by
\[4_\], or in smaller-scope workflows such as
those presented by \[3_\] and by
\[2_\], falls beyond the scope of this work.
Notably, the question of standardising imaging biomarker acquisition and
analysis is being addressed in a more comprehensive manner by groups
such as the Quantitative Imaging Biomarker Alliance
\[5_, 6_\], the Quantitative Imaging
Network \[7_, 8_\], and
task groups and committees of the American Association of Physicists in
Medicine, the European Association for Nuclear Medicine
\[9_\], the European Society of Radiology
(ESR) \[10_\], and the
European Organisation for Research and Treatment of Cancer (EORTC)
\[11_, 4_\], among others. Where
overlap exists, the reference manual refers to existing recommendations
and guidelines.

This reference manual is divided into several chapters that describe
processing of acquired imaging for high-throughput image biomarker
extraction (**Chapter [chap\_img\_proc]**); define a diverse set of
image biomarkers (**Chapter [chap\_image\_features]**); describe
guidelines for reporting on high-throughput image biomarker extraction
and an image biomarker nomenclature (**Chapter
[chap\_report\_guidelines]**); describe the benchmark data sets
(**Chapter [chap\_benchmark sets]**); and the associated benchmark
values for software verification (**Chapter [chap\_benchmarks]**).

.. [1] `Atkinson A.J., Jr, Colburn, W. A., DeGruttola, V. G., DeMets, D. L., Downing, G. J., Hoth, D. F., et al.; *Biomarkers and surrogate endpoints: Preferred definitions and conceptual framework*; Clinical Pharmacology and Therapeutics; 2001; 69 (3); 89--95 <https://doi.org/10.1067/mcp.2001.113989>`_
.. [2] `Lambin, Philippe, Leijenaar, Ralph T. H., Deist, Timo M., Peerlings, Jurgen, de Jong, Evelyn E. C., van Timmeren, Janita, et al.; *Radiomics: the bridge between medical imaging and personalized medicine.*; Nature reviews. Clinical oncology; 2017; 14 (12); 749--762 <http://www.ncbi.nlm.nih.gov/pubmed/28975929>`_
.. [3] `Caicedo, Juan C., Cooper, Sam, Heigwer, Florian, Warchal, Scott, Qiu, Peng, Molnar, Csaba, et al.; *Data-analysis strategies for image-based cell profiling*; Nature Methods; 2017; 14 (9); 849--863 <https://doi.org/10.1038/nmeth.4397>`_
.. [4] `O'Connor, James P. B., Aboagye, Eric O., Adams, Judith E., Aerts, Hugo J. W. L., Barrington, Sally F., Beer, Ambros J., et al.; *Imaging biomarker roadmap for cancer studies*; Nature Reviews Clinical Oncology; 2017; 14 (3); 169--186 <http://dx.doi.org/10.1038/nrclinonc.2016.162>`_
.. [5] `Sullivan, Daniel C, Obuchowski, Nancy A, Kessler, Larry G, Raunig, David L, Gatsonis, Constantine, Huang, Erich P, et al.; *Metrology Standards for Quantitative Imaging Biomarkers.*; Radiology; 2015; 277 (3); 813--25 <http://www.ncbi.nlm.nih.gov/pubmed/26267831>`_
.. [6] `Mulshine, James L, Gierada, David S, Armato, Samuel G, Avila, Rick S, Yankelevitz, David F, Kazerooni, Ella A, et al.; *Role of the Quantitative Imaging Biomarker Alliance in optimizing CT for the evaluation of lung cancer screen-detected nodules.*; Journal of the American College of Radiology; 2015; 12 (4); 390--5 <http://www.ncbi.nlm.nih.gov/pubmed/25842017>`_
.. [7] `Clarke, Laurence P, Nordstrom, Robert J, Zhang, Huiming, Tandon, Pushpa, Zhang, Yantian, Redmond, George, et al.; *The Quantitative Imaging Network: NCI's Historical Perspective and Planned Goals.*; Translational oncology; 2014; 7 (1); 1--4 <http://www.ncbi.nlm.nih.gov/pubmed/24772201>`_
.. [8] Nordstrom, Robert J; *The Quantitative Imaging Network in Precision Medicine*; Tomography; 2016; 2 (4); 239
.. [9] `Boellaard, Ronald, Delgado-Bolton, Roberto, Oyen, Wim J. G., Giammarile, Francesco, Tatsch, Klaus, Eschner, Wolfgang, et al.; *FDG PET/CT: EANM procedure guidelines for tumour imaging: version 2.0.*; European journal of nuclear medicine and molecular imaging; 2015; 42 (2); 328--54 <http://www.ncbi.nlm.nih.gov/pubmed/25452219>`_
.. [10] `(ESR), European Society of Radiology; *ESR statement on the stepwise development of imaging biomarkers.*; Insights into imaging; 2013; 4 (2); 147--52 <http://www.ncbi.nlm.nih.gov/pubmed/23397519>`_
.. [11] `Waterton, John C, Pylkkanen, Liisa; *Qualification of imaging biomarkers for oncology drug development.*; European journal of cancer; 2012; 48 (4); 409--15 <http://www.ncbi.nlm.nih.gov/pubmed/22226478>`_