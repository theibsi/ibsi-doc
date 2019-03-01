Introduction
============

A biomarker is “*a characteristic that is objectively measured and
evaluated as an indicator of normal biological processes, pathogenic
processes, or pharmacologic responses to a therapeutic
intervention*” :cite:`Atkinson2001`. Biomarkers may be
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
:cite:`Lambin2017`, but the scarceness of consensus
guidelines and definitions has led to it being described as a “wild
frontier” :cite:`Caicedo2017`. This reference manual
therefore presents an effort to chart a course through part of this
frontier by presenting consensus-based recommendations, guidelines,
benchmarks and definitions for image biomarker extraction, and thus
increase the reproducibility of studies involving radiomics.

We opted for a specific focus on image biomarker extraction from
acquired imaging. Thus, imaging biomarker validation, viewed in a
broader framework such as the one presented by
:cite:`OConnor2016`, or in smaller-scope workflows such as
those presented by :cite:`Caicedo2017` and by
:cite:`Lambin2017`, falls beyond the scope of this work.
Notably, the question of standardising imaging biomarker acquisition and
analysis is being addressed in a more comprehensive manner by groups
such as the Quantitative Imaging Biomarker Alliance
:cite:`Sullivan2015,Mulshine2015`, the Quantitative Imaging
Network :cite:`Clarke2014,nordstrom2016quantitative`, and
task groups and committees of the American Association of Physicists in
Medicine, the European Association for Nuclear Medicine
:cite:`Boellaard2015`, the European Society of Radiology
(ESR) :cite:`EuropeanSocietyofRadiologyESR2013`, and the
European Organisation for Research and Treatment of Cancer (EORTC)
:cite:`Waterton2012,OConnor2016`, among others. Where
overlap exists, the reference manual refers to existing recommendations
and guidelines.

This reference manual is divided into several chapters that describe
processing of acquired imaging for high-throughput image biomarker
extraction (:ref:`chap_img_proc`); define a diverse set of
image biomarkers (:ref:`chap_image_features`); describe
guidelines for reporting on high-throughput image biomarker extraction
and an image biomarker nomenclature 
(:ref:`chap_report_guidelines`); describe the benchmark data sets
(:ref:`chap_benchmark_sets`); and the associated benchmark
values for software verification (:ref:`chap_benchmarks`).
