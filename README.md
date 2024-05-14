# Text Converter V1.1 for programmers (GUI in Korean)
Written by SangDo_Kim
This program converts various text to a form frequently used in Python programmings, like list, dictionary,
unicode escape sequence, white space characters.
이 프로그램은 다양한 텍스트를 파이썬 프로그램에서 자주 사용되는 형식으로 변환합니다
예: 리스트, 딕셔너리, 유니코드 이스케이프 시퀀스, 공백 문자

![Alt text](Text_Converter_V1/demo_image.jpg)

Example:
- Tab indented string to list:
Kitchen
	Cutting Board
	Knife Set
		Long knife
		Short knife
Living Room
	Sofas
	Chairs
Bedroom
-->
[
	"Kitchen",
	[
		"Cutting Board",
		"Knife Set",
		[
			"Long knife",
			"Short knife"
		]
	],
	"Living Room",
	[
		"Sofas",
		"Chairs"
	],
	"Bedroom"
]

- Tab indented string to dictionary:
Kitchen
	Cutting Board
Living Room
	Sofas
Bedroom
-->
{
	"Kitchen": "Cutting Board",
	"Living Room": "Sofas",
	"Bedroom": Null
}

- String with unicode escape sequence to string with human-readable characters:
QLabelWidget.setText(u"\uc6d0\ubcf8 \ub0b4\uc6a9\uc744 \uc9c0\uc6c1\ub2c8\ub2e4.")
-->
QLabelWidget.setText(u"원본 내용을 지웁니다.")

- String with white space characters to string with white space escape character:
Kitchen
	Cutting Board
	Knife Set
-->
"Kitchen\n\tCutting Board\n\tKnife Set"

V1.1
- Added unicode sequence converter, list converter, dictionary converter
