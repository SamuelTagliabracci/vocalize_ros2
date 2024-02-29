# vocalize_ros2

# Install

sudo apt update

sudo apt install espeak

espeak "Hey, This is a Test."

sudo apt install python3-dev

sudo apt install build-essential

sudo apt install python3-pip

##pip3 install torch==1.8.0+cu101 torchvision==0.9.0+cu101 torchaudio===0.8.0 -f https://download.pytorch.org/whl/torch_stable.html

##pip3 install jieba

pip3 install TTS

#Running tts
tts --text "Ahh. You finally arrived. Welcome to the dark side. We have been waiting." --out_path test.wav --model_name "tts_models/en/vctk/vits" --speaker_idx p270

tts --text "Hello coqui ai fans this is a voice you can make say what you desire." --model_name "tts_models/en/ljspeech/speedy-speech-wn"  --out_path foo.wav

#tts web gui server
tts-server --model_name "tts_models/en/vctk/vits"
http://127.0.0.1:5002

# VCTK/VITS Voices
ID	NAME	AGE	GENDER	ACCENTS REGION COMMENT
0	ED		F	
1	p225	23 	F	English, Southern, England
2	p226	22 	M	English, Surrey
3	p227	38 	F	English, Cumbria
4	p228	22 	M	English, Southern, England
5	p229	23 	M	English, Southern, England
6	p230	22 	M	English, Stockton-on-tees
7	p231	23 	M	English, Southern, England
8	p232	23 	M	English, Southern, England
9	p233	23 	M	English, Staffordshire
10	p234	22 	M	Scottish, West, Dumfries
11	p236	23 	M	English, Manchester
12	p237	22 	F	Scottish, Fife
13	p238	22 	M	NorthernIrish, Belfast
14	p239	22 	M	English, SW, England
15	p240	21 	F	English, Southern, England
16	p241	21 	M	Scottish, Perth
17	p243	22 	F	English, London
18	p244	22 	F	English, Manchester
19	p245	25 	F	Irish, Dublin
20	p246	22 	F	Scottish, Selkirk
21	p247	22 	F	Scottish, Argyll
22	p248	23 	F	Indian
23	p249	22 	F	Scottish, Aberdeen
24	p250	22 	F	English, SE, England
25	p251	26 	M	Indian
26	p252	22 	M	Scottish, Edinburgh
27	p253	22 	M	Welsh, Cardiff
28	p254	21 	M	English, Surrey
29	p255	19 	M	Scottish, Galloway
30	p256	24 	M	English, Birmingham
31	p257	24 	F	English, Southern, England
32	p258	22 	M	English, Southern, England
33	p259	23 	F	English, Nottingham
34	p260	21 	F	Scottish, Orkney
35	p261	26 	F	NorthernIrish, Belfast
36	p262	23 	M	Scottish, Edinburgh
37	p263	22 	F	Scottish, Aberdeen
38	p264	23 	M	Scottish, West, Lothian
39	p265	23 	M	Scottish, Ross
40	p266	22 	M	Irish, Athlone
41	p267	23 	M	English, Yorkshire
42	p268	23 	F	English, Southern, England
43	p269	20 	M	English, Newcastle
44	p270	21 	F	English, Yorkshire
45	p271	19 	F	Scottish, Fife
46	p272	23 	M	Scottish, Edinburgh
47	p273	23 	F	English, Suffolk
48	p274	22 	F	English, Essex
49	p275	23 	F	Scottish, Midlothian
50	p276	24 	F	English, Oxford
51	p277	23 	F	English, NE, England
52	p278	22 	F	English, Cheshire
53	p279	23 	M	English, Leicester
54	p280	25 	F	Unknown, France (mic2 files unavailable)
55	p281	29 	M	Scottish, Edinburgh
56	p282	23 	M	English, Newcastle
57	p283	24 	F	Irish, Cork
58	p284	20 	F	Scottish, Fife
59	p285	21 	M	Scottish, Edinburgh
60	p286	23 	M	English, Newcastle
61	p287	23 	M	English, York
62	p288	22 	F	Irish, Dublin
63	p292	23 	M	NorthernIrish, Belfast
64	p293	22 	F	NorthernIrish, Belfast
65	p294	33 	F	American, San, Francisco
66	p295	23 	F	Irish, Dublin
67	p297	20 	F	American, New, York
68	p298	19 	M	Irish, Tipperary
69	p299	25 	M	American, California
70	p300	23 	F	American, California
71	p301	23 	M	American, North, Carolina
72	p302	20 	M	Canadian, Montreal
73	p303	24 	F	Canadian, Toronto
74	p304	22 	F	NorthernIrish, Belfast
75	p305	19 	F	American, Philadelphia
76	p306	21 	F	American, New, York
77	p307	23 	M	Canadian, Ontario
78	p308	18 	F	American, Alabama
79	p310	21 	F	American, Tennessee
80	p311	21 	F	American, Iowa
81	p312	19 	M	Canadian, Hamilton
82	p313	24 	M	Irish, County, Down
83	p314	26 	F	SouthAfrican, Cape, Town
	p315	18 	F	American, New, England, (Text and mic2 files unavailable)
84	p316	20 	F	Canadian, Alberta
85	p317	23 	M	Canadian, Hamilton
86	p318	32 	M	American, Napa
87	p323	19 	F	SouthAfrican, Pretoria
88	p326	26 	M	Australian, English, Sydney
89	p329	23 	F	American
90	p330	26 	M	American
91	p333	19 	F	American, Indiana
92	p334	18 	F	American, Chicago
93	p335	25 	F	NewZealand, English
94	p336	18 	F	SouthAfrican, Johannesburg
95	p339	21 	F	American, Pennsylvania
96	p340	18 	M	Irish, Dublin
97	p341	26 	F	American, Ohio
98	p343	27 	F	Canadian, Alberta
99	p345	22 	F	American, Florida
100	p347	26 	F	SouthAfrican, Johannesburg
101	p351	21 	F	NorthernIrish, Derry
102	p360	19 	F	American, New, Jersey
103	p361	19 	F	American, New, Jersey
104	p362	29 	F	American
105	p363	22 	F	Canadian, Toronto
106	p364	23 	F	Irish, Donegal
107	p374	28 	F	Australian, English

