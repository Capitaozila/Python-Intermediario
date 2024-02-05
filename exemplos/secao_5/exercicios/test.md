## Critérios de seleção de atributos úteis para a análise de dados, em DICOM, para o problema de classificação de imagens de mamografias

Accession Number: "A RIS generated number that identifies the order for the Study". Motivos óbvios;

Acquisition Date: "The date the acquisition of data that resulted in this image started". Motivos óbvios;

Acquisition Device Processing Code: Motivos óbvios;

Acquisition Number: Motivos óbvios;

Acquisition Time: Motivos óbvios;

Annotation Display Format ID: 'CR00' e 'Null' são os únicos atributos (não há diferenciação)/valores vazios;

Anode Target Material: 'MOLYBDENUM' e 'Null' são os únicos atributos (não há diferenciação)/valores vazios;

Attribute Modification DateTime: todos os valores são vazio;

Bits Allocated: Não há diferenciação/valores vazios;

Bits Stored: Motivos óbvios;

Body Part Thickness: "The average thickness in mm of the body part examined when compressed, if compression has been applied during exposure.". 'None' e 'Null' são os únicos atributos (não há diferenciação)/valores vazios;

Exame: Motivos óbvios, nomes de paciente, de laudo e IDs, por exemplo, não são importantes;

Body Part Examined: Motivos óbvios(todas as imagens são de mama);

Border Density: 'BLACK' e 'Null' são os únicos atributos (não há diferenciação)/valores vazios;

Breast Implant Present: não há diferenciação/valores vazios;

Burned In Annotation: 'NO' e 'Null' são os únicos atributos (não há diferenciação)/valores vazios;

Calibration Image: Não há diferenciação/valores vazios;

Code Meaning: Não há diferenciação/valores vazios;

Code Value: Não há diferenciação/valores vazios;

Coding Scheme Designator: Não há diferenciação/valores vazios;

Columns: "Number of columns in the image. Shall be an exact multiple of the horizontal downsampling factor if any of the samples (planes) are encoded downsampled in the horizontal direction for pixel data encoded in a Native (uncompressed) format. E.g., required to be an even value for a Photometric Interpretation (0028,0004) of YBR_FULL_422.". é importante;

Compression Force: 'None' e 'Null' são os únicos atributos (não há diferenciação)/valores vazios;

Content Date: "The date the image pixel data creation started. Required if image is part of a Series in which the images are temporally related. May be present otherwise. Note. This Attribute was formerly known as Image Date.". não é importante/motivos óbvios;

Content Time: "The time the Waveform data was created.". Motivos óbvio;

Contrast/Bolus Agent: Não há diferenciação(todos os valores são valores vazios);

Date of Last Calibration: "Date when the image acquisition device calibration was last changed in any way. Multiple entries may be used for additional calibrations at other times. See Section C.7.5.1.1.1 for further explanation.". não há diferenciação(todos os valores são valores vazios);

Date of Last Detector Calibration: "20220920" e vazio são os únicos atributos e não há diferenciação;

Derivation Description: "A text description of how this image was derived. See Section C.12.4.1.1 for further explanation.". é importante saber como a imagem foi derivada;

Detector Active Dimension(s): "Dimensions in mm of the active area. If Detector Active Shape (0018,7024) is: RECTANGLE: row dimension followed by column. ROUND: diameter. HEXAGONAL: diameter of a circumscribed circle." é importante;

Detector Active Shape: "RECTANGLE" e vazio são os únicos atributos e não há diferenciação;

Detector Binning: "[1,1]" e vazio são os únicos atributos e não há diferenciação;

Detector Conditions Nominal Flag: não há diferenciação(todos os valores são valores vazios);

Detector Configuration: "AREA" e vazio são os únicos atributos e não há diferenciação;

Detector Description: Motivos óbvios/não precisamos saber a descrição de cada detector;

Detector Element Physical Size: "[0.076, 0.076]" e vazio são os únicos atributos e não há diferenciação;

Detector Element Spacing: "[0.076, 0.076]" e vazio são os únicos atributos e não há diferenciação;

Detector ID: . Motivos óbvios/não precisamos saber o ID de cada detector;

Detector Temperature: não é importante;

Detector Type: "SCINTILLATOR" e vazio são os únicos atributos e não há diferenciação;

Deviation Index: "A scaled representation of the difference of the Exposure Index compared to the Target Exposure Index as defined in IEC 62494-1 and the report of AAPM TG 116.". É importante;

Device Serial Number: não é importante/valores vazios;

Distance Source to Detector: "660" e vazio são os únicos atributos e não há diferenciação;

Distance Source to Patient: "660" e vazio são os únicos atributos e não há diferenciação;

Estimated Radiographic Magnification Factor: "1.0" e vazio são os únicos atributos e não há diferenciação;

Ethnic Group: não há diferenciação(todos os valores são valores vazios);

Exposure: "80" e vazio são os únicos atributos e não há diferenciação;

Exposure Control Mode: "AUTOMATIC" e vazio são os únicos atributos e não há diferenciação;

Exposure Control Mode Description: "AEC" e vazio são os únicos atributos e não há diferenciação;

Exposure Index: . é importante;

Exposure Status: . é importante;

Exposure Time: . é importante;

Exposure in uAs: . é importante;

Field of View Dimension(s): . é importante;

Field of View Shape: . é importante;

Film Orientation: . é importante;

Filter Material: não há diferenciação/valores vazios;

Filter Thickness Maximum: . é importante;

Filter Thickness Minimum: . é importante;

Focal Spot(s): . é importante;

Gantry ID:

Grid: não há diferenciação/valores vazios;

High Bit: "Most significant bit for pixel sample data. Each sample shall have the same high bit. High Bit (0028,0102) shall be one less than Bits Stored (0028,0101). See PS3.5 for further explanation." é importante;

Imagem comments: é importante;

Image Display Format: é importante;

Image Laterality: é importante para identificar;

Image Type: é importante;

Image and Fluoroscopy Area Dose Product: é importante;

Imager Pixel Spacing: é importante;

Immages in Acquisition: é importante;

Instance Number: "A number that identifies this image." é importante;

Instituition Name: Motivos óbvios;

Institutional Department Name: Motivos óbvios;

Issuer of Patient ID: "Identifier of the Assigning Authority (system, organization, agency, or department) that issued the Patient ID." Motivos óbvios;

KVP: Motivos óbvios/ não vamos trabalhar com imagens;

Laterality: é importante;

Lossy Image Compression: é importante;

Manufacturer: "Manufacturer of the device" Motivos óbvios;

Manufacturer Model Name: "Manufacturer's model name of the device" Motivos óbvios;

Modality: Não consigo indentificar sua importância;

Modifying System: Não consigo indentificar sua importância;

Number of Frames: Não há diferenciação/valores vazios;

Operators' Name: Não consigo indentificar sua importância;

Organ Dose: Não consigo indentificar sua importância;
"
Organ Exposed: "Organ to which Organ Dose (0040,0316) applies." Sua importância é relativa, já que todo exame de mamografia é feito na mama;

Other Patient IDs: "Other identifiers for the Patient." Motivos óbvios/valores vazios;

Other Patient Names: "Other names for the Patient." Motivos óbvios/valores vazios;

Partial View: valores vazios;

Partial View Description: valores vazios;

Patient Comments: valores vazios;

Patient ID: motivos óbvios;

Patient Orientation:

Patient's Age: Útil para identificar;

Patient's Birth Date: motivos óbvios;

Patient's Name: motivos óbvios;

Patient's Sex: motivos óbvios, pois a incidência de câncer de mama acontece, na sua grande maioria, em mulheres;

Performed Procedure Step Description: valores vazios;

Performed Procedure Step ID: valores vazios;

Performing Physician's Name: valores vazios;

Photometric Interpretation: "MONOCHROME1" e "MONOCHROME2" são os únicos atributos (não há diferenciação)/valores vazios; "In particular this means that the values of Rows, Columns, Bits Stored, Bits Allocated, High Bit, Pixel Representation, Samples per Pixel, Photometric Interpretation and Planar Configuration applicable to all of the frames needs to be the same. In special cases, such as where Bits Stored is less than Bits Allocated but varies per frame, it may be safe to use the largest value for all the frames and ensure that any unused high bits are appropriately masked before encoding. It is not expected that source images with different numbers of Rows and Columns will be combined (by padding the periphery of images smaller than the largest); quite apart from not being the intended use case, this has the potential to greatly expand the size of the instance, and might also require adjustment of the Image Position (Patient) values. If the value of Photometric Interpretation in the source single frame images is not permitted for the Enhanced Multi-frame image IOD, lossless conversion of the PixelData and updating of the related Attributes is required, e.g., from MONOCHROME1 to MONOCHROME2."

---

Pixel Intensity Relationship: "LIN" e vazio são os únicos atributos e não há diferenciação;

Pixel Intensity Relationship Sign: "-1" e vazio são os únicos atributos e não há diferenciação;

Pixel Padding Range Limit: "1" e vazio são os únicos atributos e não há diferenciação;

Pixel Padding Value: "0" e vazio são os únicos atributos e não há diferenciação;

Pixel Representation: não há diferenciação(todos os valores são "0");

Pixel Spacing: é importante;

Plate ID: motivos óbvios;

Positioner Primary Angle: "0" e vazio são os únicos atributos e não há diferenciação;

Positioner Secondary Angle: "None" e vazio são os únicos atributos e não há diferenciação;

Positioner Type: "MAMMOGRAPHIC" e "NONE" são os únicos atributos e não há diferenciação;

Presentation Intent Type: "FOR PRESENTATION" e vazio são os únicos atributos e não há diferenciação;

Presentation LUT Shape: é importante;

Private Creator: "FDMS 1.0" e vazio são os únicos atributos e não há diferenciação;

Private tag data: "1" e "b'01'" são os únicos atributos e não há diferenciação;

Protocol Name: "Mammography Routine" e vazio são os únicos atributos e não há diferenciação, além disso é fútil ja que todos os exames são de mamografia;

Quality Control Image: não há diferenciação/valores vazios;

Reason for the Attribute Modification: não há diferenciação/valores vazios;

Referenced SOP Class UID: não há diferenciação/valores vazios;

Referenced SOP Instance UID: não há diferenciação/valores vazios;

Referring Physician's Name: não há diferenciação/valores vazios;

Requested Procedure ID: não há diferenciação/valores vazios;

Requesting Service: não há diferenciação/valores vazios;

Rescale Intercept: não há diferenciação(todos os valores são "0");

Rescale Slope: não há diferenciação(todos os valores são "1");

Rescale Type: não há diferenciação(todos os valores são "US");

Rows: "Shall be an exact multiple of the vertical downsampling factor if any of the samples (planes) are encoded downsampled in the vertical direction for pixel data encoded in a Native (uncompressed) format. E.g., required to be an even value for a Photometric Interpretation (0028,0004) of YBR_FULL_422." é importante;

SOP Class UID: não há diferenciação(todos os valores são "1.2.840.10008.5")

SOP Instance UID: por motivos óbvios não precisamos desse ID;

Samples per Pixel: "1" e vazio são os únicos atributos e não há diferenciação;

Scheduled Procedure Step Description: não há diferenciação/valores vazios;

Scheduled Procedure Step ID: não há diferenciação/valores vazios;

Sensitivity: "this value is manufacturer-specific. DICOM specifies Standard Attributes in Table 10-23 'Exposure Index Macro', which are recommended." é importante;

Series Date: "The date the Series started." não é importante;

Series Description: "A description of the Series." não é importante;

Series Instance UID: "A unique identifier for the Series." não é importante;

Series Number: "A number that identifies this Series." não é importante;

Series Time: "The time the Series started." não é importante;

Software Versions: "The version of the software that produced the image." é importante;

Source of Previous Values: "The source of the values in the Attributes of the current instance." não é importante;

Spatial Resolution: "The extent to which the spatial locations of all pixels are preserved during the processing of the source image that resulted in the current image" é importante, porém não há diferenciação(valores vazios);

Specific Character Set: não há diferenciação(todos os valores são "ISO_IR 100");

Station Name: "User defined name identifying the machine that produced the Composite Instances." não é importante;

Study Comments: "Comments related to the Study." valores vazios ou "MAMOGRAFIA;

Study Date: "The date the Study started." não é importante;

Study Description: "A description of the Study." "Mammography Routine" e vazio são os únicos atributos e não há diferenciação;

Study ID: "A number that identifies this Study." não é importante;

Study Instance UID: "A unique identifier for the Study." não é importante;

Study Time: "The time the Study started." não é importante;

Target Exposure Index: "The target value used to calculate Deviation Index (0018,1413) as defined in IEC 62494-1." é importante;

Time of Last Calibration: "Time when the image acquisition device calibration was last changed in any way. Multiple entries may be used. See Section C.7.5.1.1.1 for further explanation." é importante, porém não há diferenciação(valores vazios);

Time of Last Detector Calibration: "Time when the detector calibration was last changed in any way. Multiple entries may be used. See Section C." é importante;

Trim: "NO" e vazio são os únicos atributos e não há diferenciação;

View Position: "CC" e "MLO" são os únicos atributos e não há diferenciação, porém é importante;

Window Center: "The center of the window in Hounsfield units or other scale." é importante;

Window Width: "The width of the window in Hounsfield units or other scale." é importante;

X-Ray Tube Current: "The current in milliAmperes used in the X-Ray tube." é importante, porém "100" e vazio são os únicos atributos e não há diferenciação;

[Blackening Process Flag]: "0" e "1" são os únicos atributos e não há diferenciação, não encontrei dados que explicasse o que é, deve ser importante;

[Data Compression Code]: " The value of the "compression ratio" is encoded as a numeric value that represents the numerator of an implicit ratio in which the denominator is always one, consistent with the traditional representation in the literature. Note: For example, a compression ratio of 30:1 would be described with a value of 30." é importante;

[Distribution Code]: "12345678" e vazio são os únicos atributos e não há diferenciação, não encontrei dados que explicasse o que é, não é importante;

[EDR Mode]: não encontrei dados que explicasse a tag, porém "0" e vazio são os únicos atributos e não há diferenciação;

[Equipment Type-Specific Information]: não encontrei dados que explicasse a tag, porém "none" e vazio são os únicos atributos e não há diferenciação;

[Exposure Unit Type Code]: não encontrei dados que explicasse a tag. porém "F3" e vazio são os únicos atributos e não há diferenciação;

[Extended Reading Size Value]: não encontrei dados que explicasse a tag, porém "0A", "2B", "1B" e vazio são os únicos atributos;

[FCR Image ID]: não encontrei dados que explicasse a tag;

[FNC Parameters]: não encontrei dados que explicasse a tag, porém "ACC0.5" e vazio são os únicos atributos e não há diferenciação;

[Film Annotation Character String 2]: não há diferenciação/valores vazios;

[Film Output Format]: "10" e vazio são os únicos atributos e não há diferenciação;

[Film UID]: não é importante;

[Image Display Information Version No.]: não encontrei dados que explicasse a tag;

[Image No. in the Set]: não encontrei dados que explicasse a tag;

[Image Position Specifying Flag]: "1", "2" e vazio são os únicos atributos e não encontrei dados que explicasse a tag;

[Image Processing Modification Flag]: "0" e vazio são os únicos atributos e não há diferenciação;

[Image Processing Type]: "RT" e vazio são os únicos atributos e não há diferenciação;

[Image Scanning Direction]: não encontrei dados que explicasse a tag;

[Image UID]: não é importante;

[Kanji Body Part for Exposure]: não há diferenciação/valores vazios;

[Kanji Department Name]: não há diferenciação/valores vazios/não é importante;

[Kanji Hospital Name]: não há diferenciação/valores vazios/não é importante;

[Kanji Menu Name]: não há diferenciação/valores vazios/não é importante;

[Line Density Code]: "K4" e "K2" são os únicos atributos e não há diferenciação, não encontrei dados que explicasse a tag;

[Mag./Reduc. Ratio]: "100" e vazio são os únicos atributos e não há diferenciação, não encontrei dados que explicasse a tag;

[Pair Processing Information]: não encontrei dados que explicasse a tag;

[Patient Information Version No.]: "0", "256" e vazio são os únicos atributos e não há diferenciação, não encontrei dados que explicasse a tag;

[Processing Information Flag]: não encontrei dados que explicasse a tag;

[Radiographer's Code]: não encontrei dados que explicasse a tag, não há diferenciação/valores vazios;

[Reading Gain Gp]: não encontrei dados que explicasse a tag;

[Reading Sensitivity Center]: "0" e vazio são os únicos atributos e não há diferenciação, não encontrei dados que explicasse a tag;

[Relative Light Emission Amount Sk]: não encontrei dados que explicasse a tag;

[Route Image UID]: não encontrei dados que explicasse a tag, não é importante;

[Set No.]: não encontrei dados que explicasse a tag, não há diferenciação/valores vazios;

[Term of Correction for Each IP Type St]: não encontrei dados que explicasse a tag, "0" e vazio são os únicos atributos e não há diferenciação;