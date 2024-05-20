"""JAV_ProdCode_V1.31
문자열(파일 기본 이름, 확장자 제외)을 받아서 JAV 품명 코드를 추출해서 반환. 오류 시 NoCodeError 오류 발생
Example import statement:
from sangdo_mod.JAV_prod_code import JAV_prod_code, NoCodeError

V1.12 변경 사항
- 품번 인식: 특수 문자(@, $, ', & 등)이 포함된 파일 이름에서 품번 인식을 제대로 하지 못함.
예) HD@JUL-333의 품번을 HDJUL-333으로 잘못 인식했음. 이를 JUL-333로 바로 잡음.

V1.13 변경 사항
- 품번 인식: 품번 뒤에 대시가 또 붙어 있는 경우 품번 인식 오류
   예) JUL-333-Uncensored.mp에서 품번을 JUL-333-으로 잘못 인식하던 것을 바로 잡음.

V1.14 변경 사항
- 품번 인식 개선

V1.15 변경 사항
- Tokyo-Hot-n3232, 550ENE-323 등 특수 품번 처리

V1.3 변경 사항
- 클래스로 변환
- 이름 표기법 변경

V1.31 변경 사항
- 모듈 이름 변경
"""

class NoCodeError(Exception):
    pass


class JAVProdCode():
    def __init__(self):
        self.non_codes = [
            "'", "!", "#", "$", "%", "&", "(", ")", "*", ",", ".", "@",
            "[", "[", "^", "_", "`", "{", "}", "+", "=", "출)"
            ]

        #특수 품번 처리(FC2, 550ENE-154, T28-111 등에 대해 코드 앞 부분의 숫자를 영문자로 대체하여, 나중에 split()으로 분리되지 않도록 함.
        self.special_codes = [
            ["550ENE", "FiveFiveZeroENE"], ["T28", "TTwoEight"], ["S2MBD", "STwoMBD"],
            ["S2M", "STwoM"], ["FC2-PPV", "FCTwoPPV"], ["FC2PPV", "FCTwoPPV"],
            ["FC2 PPV", "FCTwoPPV"], ["1P", "OneP"],
            ["TOKYO HOT N", "TokyoHotN"], ["TOKYO-HOT-N", "TokyoHotN"]
            ]

        # 비디오 형식. 모두 소문자로 써야 함.
        self.formats_video = [
            "3g2", "3gp", "3gp2", "3gpp", "amr", "amv", "asf", "avi", "bdmv",
            "d2v", "divx", "drc", "dsa", "dsm", "dss", "dsv", "evo", "f4v", "flc",
            "fli", "flic", "flv", "hdmov", "ifo", "ivf", "m1v", "m2p", "m2t", "m2ts",
            "m2v", "m4v", "mkv", "mp2v", "mp4", "mp4v", "mpe", "mpeg", "mpg", "mpls",
            "mpv2", "mpv4", "mov", "mts", "ogm", "ogv", "pss", "pva", "qt", "ram", "ratdvd",
            "rm", "rmm", "rmvb", "roq", "rpm", "smil", "smk", "swf", "tp", "tpr", "ts", "vob",
            "vp6", "webm", "wm", "wmp", "wmv", "ts", "mts"
            ]

        self.formats_sub = ["srt", "smi", "vtt"]
        self.formats_video_sub = self.formats_video + self.formats_sub


    def get_prod_code(self, file_base_name):        
        prod_code = ""
        file_base_name = file_base_name.upper()

        # 품번에 포함될 수 없는 문자열들을 다른 문자로 교체
        for non_code in self.non_codes:
            file_base_name = file_base_name.replace(non_code, " X ")

        # 영문자, 숫자, 대시를 제외한 일어, 한국어는 모두 공백으로 교체
        for i in range(len(file_base_name)):
            if file_base_name[i].encode().isalpha() or file_base_name[i].isdecimal() or file_base_name[i] == "-":
                continue
            else:
                file_base_name = file_base_name.replace(file_base_name[i], " ")

        # 특수 코드 2번 열 추출
        special_codesCol1 = [sItem[1] for sItem in self.special_codes]
        for i in range(len(self.special_codes)):
            file_base_name = file_base_name.replace(self.special_codes[i][0], self.special_codes[i][1])

        # 문자열을 숫자(d), 영문자(a), 대시(-)별로 구분. 중간에 공백 삽입 후 split())
        char_type_prev = ""
        char_type_curr = ""
        prod_code_prefix = ""
        prod_code_suffix = ""
        file_base_nameMod = ""
        for i in range(len(file_base_name)):
            # 현재 문자 유형 검사
            if file_base_name[i].isalpha():
                char_type_curr = "d"
            elif file_base_name[i].isdecimal():
                char_type_curr = "a"
            elif file_base_name[i] == "-":
                char_type_curr = "-"
            else:
                char_type_curr = ""
            if char_type_prev != char_type_curr:
                file_base_nameMod += " "
                char_type_prev = char_type_curr
            file_base_nameMod += file_base_name[i]

        # 인덱스 오류를 방지하기 위해 앞뒤에 더미 문자 삽입.
        file_base_nameMod = "& " + file_base_nameMod + " & & & &"
        string_splits = file_base_nameMod.split()

        # 1P 품번 처리(예: 1P-072023-001)
        if "OneP" in string_splits:
            prod_code_prefix = "OneP"
            one_p_position = string_splits.index("OneP")
            while True:
                # 1P-072023 형태인 경우
                if string_splits[one_p_position+1] == "-" and string_splits[one_p_position+2].isdecimal():
                    one_p_position += 1

                if string_splits[one_p_position+1].isdecimal():
                    prod_code_suffix = string_splits[one_p_position+1]
                else:
                    prod_code_prefix = ""
                    prod_code_suffix = ""
                    break
                one_p_position += 1

                # 1P-072023-001 형태인 경우
                if string_splits[one_p_position+1] == "-" and string_splits[one_p_position+2].isdecimal():
                    prod_code_suffix += "-"
                    one_p_position += 1
                elif string_splits[one_p_position+1].isdecimal():
                    prod_code_suffix += "-"
                if string_splits[one_p_position+1].isdecimal():
                    prod_code_suffix += string_splits[one_p_position+1]
                else:
                    prod_code_prefix = ""
                    prod_code_suffix = ""
                    break
                break

            # 1P-072023-001에서 1P- 이후 뒷자리가 10자리 미만이면 품번으로 인정 안 함.
            # 나중에 self.prod_code 길이 제한으로 오류 발생될 예정
            if len(prod_code_suffix) < 10:
                prod_code_suffix = ""        

        #일반 품번 추출(예: JUL-333). 위 단계에서 품번을 추출하지 못한 경우에만 실행.
        if not prod_code_prefix:
            dash_search_point = 0
            for dash_no in range(string_splits.count("-")):
                dash_position = string_splits.index("-", dash_search_point)
                if string_splits[dash_position-1].isalpha() and string_splits[dash_position+1].isdecimal():
                    # 품번 불인정 대상: 1글자보다 작은 영문자, 1자리 숫자, 합쳐서 4글자 이하
                    if (
                            len(string_splits[dash_position-1]) <= 1
                            or len(string_splits[dash_position+1]) <= 1
                            or (len(string_splits[dash_position-1]) + len(string_splits[dash_position+1]) <= 4)):
                        if dash_no < string_splits.count("-") - 1:
                            dash_search_point = string_splits.index("-", dash_position + 1)
                            continue
                        break
                    prod_code_prefix = string_splits[dash_position-1]
                    prod_code_suffix = string_splits[dash_position+1]
                else:
                    if dash_no < string_splits.count("-") - 1:
                        dash_search_point = string_splits.index("-", dash_position + 1)
                        continue
                    else:
                        break

        #대시가 없는 파일 이름에서 임의로 대시를 붙여 품번 생성
        if not prod_code_prefix: 
            for i in range(len(string_splits)):
                if string_splits[i].isdecimal() and len(string_splits[i]) >= 2:       
                    if (
                            string_splits[i-1].isalpha() 
                            and (2 <= len(string_splits[i-1]) <= 6) 
                            or string_splits[i-1] in special_codesCol1):
                        if (
                                (5 <= len(string_splits[i-1]) + len(string_splits[i]) <= 6) 
                                or string_splits[i-1] in special_codesCol1):
                            #합쳐서 5~6글자 품번만 임의 대시 부착 품번 인정
                            prod_code_prefix = string_splits[i - 1]
                            prod_code_suffix = string_splits[i]
                        else:
                            continue

        #최종 품번을 만들기 및 글자 수 등 점검
        if prod_code_prefix == "TokyoHotN":
            prod_code = prod_code_prefix + prod_code_suffix
        elif prod_code_prefix != "" and prod_code_suffix != "":
            prod_code = prod_code_prefix + "-" + prod_code_suffix

        # 특수 코드(예:550ENE) 복원
        for i in range(len(self.special_codes)):
            prod_code = prod_code.replace(self.special_codes[i][1], self.special_codes[i][0])

        # FC2-PPV는 뒤의 숫자가 7자리임.
        if prod_code.find("FC2-PPV") >= 0 and len(prod_code_suffix) < 7:
            raise NoCodeError

        if 6 <= len(prod_code) <= 16:
            return prod_code
        else:
            raise NoCodeError

JAV_prod_code = JAVProdCode()

#테스트 실행
if __name__ == "__main__":
    #sample_file_name = ["Tokyo Hot n0501 佐野美鈴 無言輪姦三穴破壊生贄汁_ _2.6 GiB_2018-09-01 00:56_0_2_557"]
    sample_file_names = ["JUL-322", "550ENE-323", "FC2-PPV-3806605", "1P-072023-001", "Tokyo-Hot-n0588",
                       "071312-073", "EUN#-232", "EUN영상JUL-333-한국어Uncensored", "ESFF231"]
    #sample_file_name = ["Tokyo-Hot-n0588"]
    file_names = sample_file_names
    for file_name in sample_file_names:
        prod_code = (file_name)
        try:
            print(f"품번:\t{JAV_prod_code.get_prod_code(prod_code)}\t파일 이름:\t{file_name}")
        except NoCodeError:
            print(f"품번 추출 실패:\t{file_name}")
        except ValueError:
            print(f"ValueError\t파일 이름:\t{file_name}")
