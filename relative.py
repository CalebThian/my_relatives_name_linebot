# -*- coding: utf-8 -*-
"""
Created on Wed Dec 23 12:26:30 2020

@author: caleb
"""
father_father ={"caller":"祖父","callee":"孫男/孫女","caller_o" : "令祖父","caller_s" : "家祖父"}
father_mother ={"caller":"祖母","callee":"孫男/孫女","caller_o" : "令祖母","caller_s" : "家祖母"}        
father_brother_e = {"caller":"伯父","callee":"侄男/侄女","caller_o" : "令伯父","caller_s" : "家伯父"}
father_brother_y = {"caller":"叔父","callee":"侄男/侄女","caller_o" : "令叔父","caller_s" : "家叔父"}
father_brother_e_spouse = {"caller":"伯母","callee":"侄男/侄女","caller_o" : "令伯母","caller_s" : "家伯母"}
father_brother_y_spouse = {"caller":"叔母","callee":"侄男/侄女","caller_o" : "令叔母","caller_s" : "家叔母"}
father_sister_e = {"caller":"姑母","callee":"侄男/侄女","caller_o" : "令姑母","caller_s" : "家姑母"}
father_sister_y = {"caller":"姑母","callee":"侄男/侄女","caller_o" : "令姑母","caller_s" : "家姑母"}
father_sister_e_spouse = {"caller":"姑父","callee":"内侄男/侄女","caller_o" : "令姑父","caller_s" : "家姑父"}
father_sister_y_spouse = {"caller":"姑父","callee":"内侄男/侄女","caller_o" : "令姑父","caller_s" : "家姑父"}
father_nephew = {"caller":"堂兄弟","callee":"堂兄姊妹弟","caller_o" : "令堂兄弟","caller_s" : "家堂兄/家堂弟"}
father_niece = {"caller":"堂姊妹","callee":"堂兄姊妹弟","caller_o" : "令堂姊妹","caller_s" : "家堂姊/家堂妹"}
father_nephew_o = {"caller":"姑表兄弟","callee":"舅表兄姊妹弟","caller_o" : "令姑表兄弟","caller_s" : "家姑表兄/家姑表弟"}
father_niece_o = {"caller":"姑表姊妹","callee":"舅表兄姊妹弟","caller_o" : "令姑表姊妹","caller_s" : "家姑表姊/家姑表妹"}
father_son = {"caller":"同父異母兄弟","callee":"同父異母兄姊妹弟","caller_o" : "令同父異母兄弟","caller_s" : "家同父異母兄/家同父異母弟"}
father_daughter = {"caller":"同父異母姊妹","callee":"同父異母兄姊妹弟","caller_o" : "令同父異母姊妹","caller_s" : "家同父異母姊/家同父異母妹"}
father_grandpa={"caller":"曾祖父","callee":"曾孫男/曾孫女","caller_o" : "令曾祖父","caller_s" : "家曾祖父"}
father_grandma ={"caller":"曾祖母","callee":"曾孫男/曾孫女","caller_o" : "令曾祖母","caller_s" : "家曾祖母"} 
father_grandpa_o={"caller":"曾外祖父","callee":"外曾孫男/外曾孫女","caller_o" : "令曾外祖父","caller_s" : "家曾外祖父"}
father_grandma_o={"caller":"曾外祖母","callee":"外曾孫男/外曾孫女","caller_o" : "令曾外祖母","caller_s" : "家曾外祖母"} 
father_uncle_e={"caller":"伯祖父","callee":"侄孫男/侄孫女","caller_o" : "令伯祖父","caller_s" : "家伯祖父"}
father_uncle_y={"caller":"叔祖父","callee":"侄孫男/侄孫女","caller_o" : "令叔祖父","caller_s" : "家叔祖父"}
father_aunt_e={"caller":"伯祖母","callee":"夫侄孫男/夫侄孫女","caller_o" : "令伯祖母","caller_s" : "家伯祖母"}
father_aunt_y={"caller":"叔祖母","callee":"夫侄孫男/夫侄孫女","caller_o" : "令叔祖母","caller_s" : "家叔祖母"}
father_grandaunt ={"caller":"姑祖母","callee":"侄孫男/侄孫女","caller_o" : "令姑祖母","caller_s" : "家姑祖母"}
father_granduncle ={"caller":"姑祖父","callee":"内侄孫男/内侄孫女","caller_o" : "令姑祖父","caller_s" : "家姑祖父"}
father_grandaunt_oe ={"caller":"舅祖母","callee":"夫甥孫男/夫甥孫女","caller_o" : "令舅祖母","caller_s" : "家舅祖母"}
father_granduncle_oe ={"caller":"舅祖父","callee":"甥孫男/甥孫女","caller_o" : "令舅祖父","caller_s" : "家舅祖父"}
father_grandaunt_oy ={"caller":"姨祖母","callee":"甥孫男/甥孫女","caller_o" : "令姨祖母","caller_s" : "家姨祖母"}
father_granduncle_oy ={"caller":"姨祖父","callee":"内甥孫男/内甥孫女","caller_o" : "令姨祖父","caller_s" : "家姨祖父"}

mother_father ={"caller":"外祖父","callee":"外孫男/外孫女","caller_o" : "令外祖父","caller_s" : "家外祖父"}
mother_mother ={"caller":"外祖母","callee":"外孫男/外孫女","caller_o" : "令外祖母","caller_s" : "家外祖母"}        
mother_brother_e = {"caller":"舅父","callee":"甥男/甥女","caller_o" : "令舅父","caller_s" : "家舅父"}
mother_brother_y = {"caller":"舅父","callee":"甥男/甥女","caller_o" : "令舅父","caller_s" : "家舅父"}
mother_brother_e_spouse = {"caller":"舅母","callee":"夫甥男/夫甥女","caller_o" : "令舅母","caller_s" : "家舅母"}
mother_brother_y_spouse = {"caller":"舅母","callee":"夫甥男/夫甥女","caller_o" : "令舅母","caller_s" : "家舅母"}
mother_sister_e = {"caller":"姨母","callee":"甥男/甥女","caller_o" : "令姨母","caller_s" : "家姨母"}
mother_sister_y = {"caller":"姨母","callee":"甥男/甥女","caller_o" : "令姨母","caller_s" : "家姨母"}
mother_sister_e_spouse = {"caller":"姨父","callee":"内甥男/甥女","caller_o" : "令姨父","caller_s" : "家姨父"}
mother_sister_y_spouse = {"caller":"姨父","callee":"内甥男/甥女","caller_o" : "令姨父","caller_s" : "家姨父"}
mother_nephew = {"caller":"舅表兄弟","callee":"姑表兄姊妹弟","caller_o" : "令舅表兄弟","caller_s" : "家舅表兄/家舅表弟"}
mother_niece = {"caller":"舅表姊妹","callee":"姑表兄姊妹弟","caller_o" : "令舅表姊妹","caller_s" : "家舅表姊/家舅表妹"}
mother_nephew_o = {"caller":"姨表兄弟","callee":"姨表兄姊妹弟","caller_o" : "令姨表兄弟","caller_s" : "家姨表兄/家姨表弟"}
mother_niece_o = {"caller":"姨表姊妹","callee":"姨表兄姊妹弟","caller_o" : "令姨表姊妹","caller_s" : "家姨表姊/家姨表妹"}
mother_son = {"caller":"同母異父兄弟","callee":"同母異父兄姊妹弟","caller_o" : "令同母異父兄弟","caller_s" : "家同母異父兄/家同母異父弟"}
mother_daughter = {"caller":"同母異父姊妹","callee":"同母異父兄姊妹弟","caller_o" : "令同母異父姊妹","caller_s" : "家同母異父姊/家同母異父妹"}
mother_grandpa={"caller":"外曾祖父","callee":"曾外孫男/曾外孫女","caller_o" : "令外曾祖父","caller_s" : "家外曾祖父"}
mother_grandma ={"caller":"外曾祖母","callee":"曾外孫男/曾外孫女","caller_o" : "令外曾祖母","caller_s" : "家外曾祖母"} 
mother_grandpa_o={"caller":"外曾外祖父","callee":"外曾外孫男/外曾外孫女","caller_o" : "令外曾外祖父","caller_s" : "家外曾外祖父"}
mother_grandma_o={"caller":"外曾外祖母","callee":"外曾外孫男/外曾外孫女","caller_o" : "令外曾外祖母","caller_s" : "家外曾外祖母"} 
mother_uncle_e={"caller":"伯外祖父","callee":"侄外孫男/侄外孫女","caller_o" : "令伯外祖父","caller_s" : "家伯外祖父"}
mother_uncle_y={"caller":"叔外祖父","callee":"侄外孫男/侄外孫女","caller_o" : "令叔外祖父","caller_s" : "家叔外祖父"}
mother_aunt_e={"caller":"伯外祖母","callee":"夫侄外孫男/夫侄外孫女","caller_o" : "令伯外祖母","caller_s" : "家伯外祖母"}
mother_aunt_y={"caller":"叔外祖母","callee":"夫侄外孫男/夫侄外孫女","caller_o" : "令叔外祖母","caller_s" : "家叔外祖母"}
mother_grandaunt ={"caller":"姑外祖母","callee":"侄外孫男/侄外孫女","caller_o" : "令姑外祖母","caller_s" : "家姑外祖母"}
mother_granduncle ={"caller":"姑外祖父","callee":"内侄外孫男/内侄外孫女","caller_o" : "令姑外祖父","caller_s" : "家姑外祖父"}
mother_grandaunt_oe ={"caller":"舅外祖母","callee":"夫甥外孫男/夫甥外孫女","caller_o" : "令舅外祖母","caller_s" : "家舅外祖母"}
mother_granduncle_oe ={"caller":"舅外祖父","callee":"甥外孫男/甥外孫女","caller_o" : "令舅外祖父","caller_s" : "家舅外祖父"}
mother_grandaunt_oy ={"caller":"姨外祖母","callee":"甥外孫男/甥外孫女","caller_o" : "令姨外祖母","caller_s" : "家姨外祖母"}
mother_granduncle_oy ={"caller":"姨外祖父","callee":"内甥外孫男/内甥外孫女","caller_o" : "令姨外祖父","caller_s" : "家姨外祖父"}

brother_e_spouse={"caller":"兄嫂/兄姊","callee":"大伯兄/大姑姊/小叔弟/小姑妹","caller_o" : "令兄姊","caller_s" : "家兄姊"}
brother_y_spouse={"caller":"弟嫂/弟妹/弟媳","callee":"大伯弟/大姑姊/小叔弟/小姑妹","caller_o" : "令弟妹","caller_s" : "家弟妹"}
brother_son = {"caller":"侄男","callee":"叔父/伯父/姑母","caller_o" : "令侄男","caller_s" : "舍侄男"}
brother_daughter = {"caller":"侄女","callee":"叔父/伯父/姑母","caller_o" : "令侄女","caller_s" : "舍侄女"}
brother_son_in_law= {"caller":"侄婿/侄女婿","callee":"叔丈人/伯丈人/姑丈母娘","caller_o" : "令侄婿","caller_s" : "舍侄婿"}
brother_daughter_in_law= {"caller":"侄婦/侄息婦","callee":"叔丈人/伯丈人/姑丈母娘","caller_o" : "令侄婦","caller_s" : "舍侄婦"}
brother_grandson={"caller":"侄孫男","callee":"叔祖父/伯祖父/姑祖母","caller_o" : "令侄孫男","caller_s" : "舍侄孫男"}
brother_granddaughter={"caller":"侄孫女","callee":"叔祖父/伯祖父/姑祖母","caller_o" : "令侄孫女","caller_s" : "舍侄孫女"}
brother_grandson_o={"caller":"侄外孫男","callee":"叔外祖父/伯外祖父/姑外祖母","caller_o" : "令侄外孫男","caller_s" : "舍侄外孫男"}
brother_granddaughter_o={"caller":"侄外孫女","callee":"叔外祖父/伯外祖父/姑外祖母","caller_o" : "令侄外孫女","caller_s" : "舍侄外孫女"}
brother_e_father_in_law={"caller":"兄姻父/兄姻伯父","callee":"女媳姻男/女","caller_o" : "令姻伯父","caller_s" : "家姻伯父"}
brother_e_mother_in_law={"caller":"兄姻母/兄姻伯母","callee":"女媳姻男/女","caller_o" : "令姻伯母","caller_s" : "家姻伯母"}
brother_y_father_in_law={"caller":"弟姻父/弟姻伯父","callee":"女媳姻男/女","caller_o" : "令姻伯父","caller_s" : "家姻伯父"}
brother_y_mother_in_law={"caller":"弟姻母/弟姻伯母","callee":"女媳姻男/女","caller_o" : "令姻伯母","caller_s" : "家姻伯母"}
brother_e_brother_in_law_e={"caller":"兄姻兄","callee":"姊妹姻兄弟/姊妹姻姊妹","caller_o" : "令姻兄","caller_s" : "家姻兄"}
brother_e_sister_in_law_e={"caller":"兄姻姊","callee":"姊妹姻兄弟/姊妹姻姊妹","caller_o" : "令姻姊","caller_s" : "家姻姊"}
brother_y_brother_in_law_e={"caller":"弟姻兄","callee":"姊妹姻兄弟/姊妹姻姊妹","caller_o" : "令姻兄","caller_s" : "家姻兄"}
brother_y_sister_in_law_e={"caller":"弟姻姊","callee":"姊妹姻兄弟/姊妹姻姊妹","caller_o" : "令姻姊","caller_s" : "家姻姊"}
brother_e_brother_in_law_y={"caller":"兄姻弟","callee":"姊妹姻兄弟/姊妹姻姊妹","caller_o" : "令姻兄","caller_s" : "舍姻弟"}
brother_e_sister_in_law_y={"caller":"兄姻妹","callee":"姊妹姻兄弟/姊妹姻姊妹","caller_o" : "令姻姊","caller_s" : "舍姻妹"}
brother_y_brother_in_law_y={"caller":"弟姻弟","callee":"姊妹姻兄弟/姊妹姻姊妹","caller_o" : "令姻弟","caller_s" : "舍姻弟"}
brother_y_sister_in_law_y={"caller":"弟姻妹","callee":"姊妹姻兄弟/姊妹姻姊妹","caller_o" : "令姻妹","caller_s" : "舍姻妹"}
brother_e_brother_e_spouse={"caller":"兄姻兄婦","callee":"姑姊妹姻兄弟/姑姊妹姻姊妹","caller_o" : "令姻兄婦","caller_s" : "家姻兄婦"}
brother_e_brother_y_spouse={"caller":"兄姻弟婦","callee":"姑姊妹姻兄弟/姑姊妹姻姊妹","caller_o" : "令姻弟婦","caller_s" : "舍姻弟婦"}
brother_e_sister_e_spouse={"caller":"兄姻姊夫","callee":"姨姊妹姻兄弟/姨姊妹姻姊妹","caller_o" : "令姻姊夫","caller_s" : "家姻姊夫"}
brother_e_sister_y_spouse={"caller":"兄姻妹夫","callee":"姨姊妹姻兄弟/姨姊妹姻姊妹","caller_o" : "令姻妹夫","caller_s" : "舍姻妹夫"}
brother_y_brother_e_spouse={"caller":"弟姻兄婦","callee":"姑姊妹姻兄弟/姑姊妹姻姊妹","caller_o" : "令姻兄婦","caller_s" : "家姻兄婦"}
brother_y_brother_y_spouse={"caller":"弟姻弟婦","callee":"姑姊妹姻兄弟/姑姊妹姻姊妹","caller_o" : "令姻弟婦","caller_s" : "舍姻弟婦"}
brother_y_sister_e_spouse={"caller":"弟姻姊夫","callee":"姨姊妹姻兄弟/姨姊妹姻姊妹","caller_o" : "令姻姊夫","caller_s" : "家姻姊夫"}
brother_y_sister_y_spouse={"caller":"弟姻妹夫","callee":"姨姊妹姻兄弟/姨姊妹姻姊妹","caller_o" : "令姻妹夫","caller_s" : "舍姻妹夫"}
brother_e_nephew={"caller":"兄姻侄男","callee":"姑姻叔伯父/姑姻姑母","caller_o" : "令姻侄男","caller_s" : "舍姻侄男"}
brother_e_niece={"caller":"兄姻侄女","callee":"姑姻叔伯父/姑姻姑母","caller_o" : "令姻侄女","caller_s" : "舍姻侄女"}
brother_e_nephew_o={"caller":"兄姻甥男","callee":"姨姻叔伯父/姨姻姑母","caller_o" : "令姻甥男","caller_s" : "舍姻甥男"}
brother_e_niece_o={"caller":"兄姻甥女","callee":"姨姻叔伯父/姨姻姑母","caller_o" : "令姻甥女","caller_s" : "舍姻甥女"}
brother_y_nephew={"caller":"弟姻侄男","callee":"姑姻叔伯父/姑姻姑母","caller_o" : "令姻侄男","caller_s" : "舍姻侄男"}
brother_y_niece={"caller":"弟姻侄女","callee":"姑姻叔伯父/姑姻姑母","caller_o" : "令姻侄女","caller_s" : "舍姻侄女"}
brother_y_nephew_o={"caller":"弟姻甥男","callee":"姨姻叔伯父/姨姻姑母","caller_o" : "令姻甥男","caller_s" : "舍姻甥男"}
brother_y_niece_o={"caller":"弟姻甥女","callee":"姨姻叔伯父/姨姻姑母","caller_o" : "令姻甥女","caller_s" : "舍姻甥女"}

sister_e_spouse={"caller":"姊夫/姊兄","callee":"大舅兄/大姨姊/小舅弟/小姨妹","caller_o" : "令姊兄","caller_s" : "家姊兄"}
sister_y_spouse={"caller":"妹夫/妹弟","callee":"大舅弟/大姨姊/小舅弟/小姨妹","caller_o" : "令妹弟","caller_s" : "家妹弟"}
sister_son = {"caller":"甥男","callee":"舅父/姨母","caller_o" : "令甥男","caller_s" : "舍甥男"}
sister_daughter = {"caller":"甥女","callee":"舅父/姨母","caller_o" : "令甥女","caller_s" : "舍甥女"}
sister_son_in_law= {"caller":"甥婿/甥女婿","callee":"舅丈人/姨丈母娘","caller_o" : "令甥婿","caller_s" : "舍甥婿"}
sister_daughter_in_law= {"caller":"甥婦/甥息婦","callee":"舅丈人/姨丈母娘","caller_o" : "令甥婦","caller_s" : "舍甥婦"}
sister_grandson={"caller":"甥孫男","callee":"舅祖父/姨祖母","caller_o" : "令甥孫男","caller_s" : "舍甥孫男"}
sister_granddaughter={"caller":"甥孫女","callee":"舅祖父/姨祖母","caller_o" : "令甥孫女","caller_s" : "舍甥孫女"}
sister_grandson_o={"caller":"甥外孫男","callee":"舅外祖父/姨外祖母","caller_o" : "令甥外孫男","caller_s" : "舍甥外孫男"}
sister_granddaughter_o={"caller":"甥外孫女","callee":"舅外祖父/姨外祖母","caller_o" : "令甥外孫女","caller_s" : "舍甥外孫女"}
sister_e_father_in_law={"caller":"姊姻父/姊姻伯父","callee":"男媳姻男/女","caller_o" : "令姻伯父","caller_s" : "家姻伯父"}
sister_e_mother_in_law={"caller":"姊姻母/姊姻伯母","callee":"男媳姻男/女","caller_o" : "令姻伯母","caller_s" : "家姻伯母"}
sister_y_father_in_law={"caller":"妹姻父/妹姻伯父","callee":"男媳姻男/女","caller_o" : "令姻伯父","caller_s" : "家姻伯父"}
sister_y_mother_in_law={"caller":"妹姻母/妹姻伯母","callee":"男媳姻男/女","caller_o" : "令姻伯母","caller_s" : "家姻伯母"}
sister_e_brother_in_law_e={"caller":"姊姻兄","callee":"兄弟姻兄弟/兄弟姻姊妹","caller_o" : "令姻兄","caller_s" : "家姻兄"}
sister_e_sister_in_law_e={"caller":"姊姻姊","callee":"兄弟姻兄弟/兄弟姻姊妹","caller_o" : "令姻姊","caller_s" : "家姻姊"}
sister_y_brother_in_law_e={"caller":"妹姻兄","callee":"兄弟姻兄弟/兄弟姻姊妹","caller_o" : "令姻兄","caller_s" : "家姻兄"}
sister_y_sister_in_law_e={"caller":"妹姻姊","callee":"兄弟姻兄弟/兄弟姻姊妹","caller_o" : "令姻姊","caller_s" : "家姻姊"}
sister_e_brother_in_law_y={"caller":"姊姻弟","callee":"兄弟姻兄弟/兄弟姻姊妹","caller_o" : "令姻兄","caller_s" : "舍姻弟"}
sister_e_sister_in_law_y={"caller":"姊姻妹","callee":"兄弟姻兄弟/兄弟姻姊妹","caller_o" : "令姻姊","caller_s" : "舍姻妹"}
sister_y_brother_in_law_y={"caller":"妹姻弟","callee":"兄弟姻兄弟/兄弟姻姊妹","caller_o" : "令姻弟","caller_s" : "舍姻弟"}
sister_y_sister_in_law_y={"caller":"妹姻妹","callee":"兄弟姻兄弟/兄弟姻姊妹","caller_o" : "令姻妹","caller_s" : "舍姻妹"}
sister_e_brother_e_spouse={"caller":"姊姻兄婦","callee":"叔兄弟姻兄弟/叔兄弟姻姊妹","caller_o" : "令姻兄婦","caller_s" : "家姻兄婦"}
sister_e_brother_y_spouse={"caller":"姊姻弟婦","callee":"叔兄弟姻兄弟/叔兄弟姻姊妹","caller_o" : "令姻弟婦","caller_s" : "舍姻弟婦"}
sister_e_sister_e_spouse={"caller":"姊姻姊夫","callee":"舅兄弟姻兄弟/舅兄弟姻姊妹","caller_o" : "令姻姊夫","caller_s" : "家姻姊夫"}
sister_e_sister_y_spouse={"caller":"姊姻妹夫","callee":"舅兄弟姻兄弟/舅兄弟姻姊妹","caller_o" : "令姻妹夫","caller_s" : "舍姻妹夫"}
sister_y_brother_e_spouse={"caller":"妹姻兄婦","callee":"叔兄弟姻兄弟/叔兄弟姻姊妹","caller_o" : "令姻兄婦","caller_s" : "家姻兄婦"}
sister_y_brother_y_spouse={"caller":"妹姻弟婦","callee":"叔兄弟姻兄弟/叔兄弟姻姊妹","caller_o" : "令姻弟婦","caller_s" : "舍姻弟婦"}
sister_y_sister_e_spouse={"caller":"妹姻姊夫","callee":"舅兄弟姻兄弟/舅兄弟姻姊妹","caller_o" : "令姻姊夫","caller_s" : "家姻姊夫"}
sister_y_sister_y_spouse={"caller":"妹姻妹夫","callee":"舅兄弟姻兄弟/舅兄弟姻姊妹","caller_o" : "令姻妹夫","caller_s" : "舍姻妹夫"}
sister_e_nephew={"caller":"姊姻侄男","callee":"叔姻舅父/叔姻姨母","caller_o" : "令姻侄男","caller_s" : "舍姻侄男"}
sister_e_niece={"caller":"姊姻侄女","callee":"叔姻舅父/叔姻姨母","caller_o" : "令姻侄女","caller_s" : "舍姻侄女"}
sister_e_nephew_o={"caller":"姊姻甥男","callee":"舅姻舅父/舅姻姨母","caller_o" : "令姻甥男","caller_s" : "舍姻甥男"}
sister_e_niece_o={"caller":"姊姻甥女","callee":"舅姻舅父/舅姻姨母","caller_o" : "令姻甥女","caller_s" : "舍姻甥女"}
sister_y_nephew={"caller":"妹姻侄男","callee":"叔姻舅父/叔姻姨母","caller_o" : "令姻侄男","caller_s" : "舍姻侄男"}
sister_y_niece={"caller":"妹姻侄女","callee":"叔姻舅父/叔姻姨母","caller_o" : "令姻侄女","caller_s" : "舍姻侄女"}
sister_y_nephew_o={"caller":"妹姻甥男","callee":"舅姻舅父/舅姻姨母","caller_o" : "令姻甥男","caller_s" : "舍姻甥男"}
sister_y_niece_o={"caller":"妹姻甥女","callee":"舅姻舅父/舅姻姨母","caller_o" : "令姻甥女","caller_s" : "舍姻甥女"}

son_spouse={"caller":"媳婦","callee":"公公/婆婆","caller_o" : "令媳婦","caller_s" : "舍媳婦"}
son_son = {"caller":"孫男","callee":"祖父/祖母","caller_o" : "令孫男","caller_s" : "舍孫男"}
son_daughter = {"caller":"孫女","callee":"祖父/祖母","caller_o" : "令孫女","caller_s" : "舍孫女"}
son_son_in_law= {"caller":"孫婿/孫女婿","callee":"祖丈人/祖丈母娘","caller_o" : "令孫婿","caller_s" : "舍孫婿"}
son_daughter_in_law= {"caller":"孫婦/孫息婦","callee":"祖公/祖婆","caller_o" : "令孫婦","caller_s" : "舍孫婦"}
son_grandson={"caller":"曾孫男","callee":"曾祖父/曾祖母","caller_o" : "令曾孫男","caller_s" : "舍曾孫男"}
son_granddaughter={"caller":"曾孫女","callee":"曾祖父/曾祖母","caller_o" : "令曾孫女","caller_s" : "舍曾孫女"}
son_grandson_o={"caller":"曾外孫男","callee":"曾外祖父/曾外祖母","caller_o" : "令曾外孫男","caller_s" : "舍曾外孫男"}
son_granddaughter_o={"caller":"曾外孫女","callee":"曾外祖父/曾外祖母","caller_o" : "令曾外孫女","caller_s" : "舍曾外孫女"}
son_father_in_law={"caller":"男媳姻兄弟","callee":"女媳姻兄弟/姊妹","caller_o" : "令姻兄弟","caller_s" : "家姻兄/舍婚弟"}
son_mother_in_law={"caller":"男媳姻姊妹","callee":"女媳姻兄弟/姊妹","caller_o" : "令姻姊妹","caller_s" : "家姻姊/舍婚妹"}
son_brother_in_law_e={"caller":"男媳姻男","callee":"姊妹姻父/姊妹姻母","caller_o" : "令姻侄/甥男","caller_s" : "舍姻男"}
son_sister_in_law_e={"caller":"男媳姻女","callee":"姊妹姻父/姊妹姻母","caller_o" : "令姻侄/甥女","caller_s" : "舍姻女"}
son_brother_in_law_y={"caller":"男媳姻男","callee":"姊妹姻父/姊妹姻母","caller_o" : "令姻侄/甥男","caller_s" : "舍姻男"}
son_sister_in_law_y={"caller":"男媳姻女","callee":"姊妹姻父/姊妹姻母","caller_o" : "令姻侄/甥女","caller_s" : "舍姻女"}
son_brother_e_spouse={"caller":"男媳姻婦","callee":"姑姊妹姻父/姑姊妹姻母","caller_o" : "令姻侄/甥男婦","caller_s" : "舍姻婦"}
son_brother_y_spouse={"caller":"男媳姻婦","callee":"姑姊妹姻父/姑姊妹姻母","caller_o" : "令姻侄/甥男婦","caller_s" : "舍姻婦"}
son_sister_e_spouse={"caller":"男媳姻婿","callee":"姨姊妹姻父/姨姊妹姻母","caller_o" : "令姻侄/甥女婿","caller_s" : "舍姻婿"}
son_sister_y_spouse={"caller":"男媳姻婿","callee":"姨姊妹姻父/姨姊妹姻母","caller_o" : "令姻侄/甥女婿","caller_s" : "舍姻婿"}
son_nephew={"caller":"男媳姻孫男","callee":"姑姻祖父/姑姻祖母","caller_o" : "令姻孫男","caller_s" : "舍姻孫男"}
son_niece={"caller":"男媳姻孫女","callee":"姑姻祖父/姑姻祖母","caller_o" : "令姻孫女","caller_s" : "舍姻孫女"}
son_nephew_o={"caller":"男媳姻外孫男","callee":"姨姻祖父/姨姻祖母","caller_o" : "令姻外孫男","caller_s" : "舍姻外孫男"}
son_niece_o={"caller":"男媳姻外孫女","callee":"姨姻祖父/姨姻祖母","caller_o" : "令姻外孫女","caller_s" : "舍姻外孫女"}

daughter_spouse={"caller":"女婿","callee":"岳父/岳母","caller_o" : "令女婿","caller_s" : "舍女婿"}
daughter_son = {"caller":"外孫男","callee":"外祖父/外祖母","caller_o" : "令外孫男","caller_s" : "舍外孫男"}
daughter_daughter = {"caller":"外孫女","callee":"外祖父/外祖母","caller_o" : "令外孫女","caller_s" : "舍外孫女"}
daughter_son_in_law= {"caller":"外孫婿/外孫女婿","callee":"外祖丈人/外祖丈母娘","caller_o" : "令外孫婿","caller_s" : "舍外孫婿"}
daughter_daughter_in_law= {"caller":"外孫婦/外孫息婦","callee":"外祖公/外祖婆","caller_o" : "令外孫婦","caller_s" : "舍外孫婦"}
daughter_grandson={"caller":"外曾孫男","callee":"曾外祖父/曾外祖母","caller_o" : "令外曾孫男","caller_s" : "舍外曾孫男"}
daughter_granddaughter={"caller":"外曾孫女","callee":"曾外祖父/曾外祖母","caller_o" : "令外曾孫女","caller_s" : "舍外曾孫女"}
daughter_granddaughter_o={"caller":"外曾外孫男","callee":"外曾外祖父/外曾外祖母","caller_o" : "令外曾外孫男","caller_s" : "舍外曾外孫男"}
daughter_granddaughter_o={"caller":"外曾外孫女","callee":"外曾外祖父/外曾外祖母","caller_o" : "令外曾外孫女","caller_s" : "舍外曾外孫女"}
daughter_father_in_law={"caller":"女媳姻兄弟","callee":"男媳姻兄弟/姊妹","caller_o" : "令姻兄弟","caller_s" : "家姻兄/舍婚弟"}
daughter_mother_in_law={"caller":"女媳姻姊妹","callee":"男媳姻兄弟/姊妹","caller_o" : "令姻姊妹","caller_s" : "家姻姊/舍婚妹"}
daughter_brother_in_law_e={"caller":"女媳姻男","callee":"兄弟姻父/兄弟姻母","caller_o" : "令姻侄/甥男","caller_s" : "舍姻男"}
daughter_sister_in_law_e={"caller":"女媳姻女","callee":"兄弟姻父/兄弟姻母","caller_o" : "令姻侄/甥女","caller_s" : "舍姻女"}
daughter_brother_in_law_y={"caller":"女媳姻男","callee":"兄弟姻父/兄弟姻母","caller_o" : "令姻侄/甥男","caller_s" : "舍姻男"}
daughter_sister_in_law_y={"caller":"女媳姻女","callee":"兄弟姻父/兄弟姻母","caller_o" : "令姻侄/甥女","caller_s" : "舍姻女"}
daughter_brother_e_spouse={"caller":"女媳姻婦","callee":"叔兄弟姻父/叔兄弟姻母","caller_o" : "令姻侄/甥男婦","caller_s" : "舍姻婦"}
daughter_brother_y_spouse={"caller":"女媳姻婦","callee":"叔兄弟姻父/叔兄弟姻母","caller_o" : "令姻侄/甥男婦","caller_s" : "舍姻婦"}
daughter_sister_e_spouse={"caller":"女媳姻婿","callee":"舅兄弟姻父/舅兄弟姻母","caller_o" : "令姻侄/甥女婿","caller_s" : "舍姻婿"}
daughter_sister_y_spouse={"caller":"女媳姻婿","callee":"舅兄弟姻父/舅兄弟姻母","caller_o" : "令姻侄/甥女婿","caller_s" : "舍姻婿"}
daughter_nephew={"caller":"女媳姻孫男","callee":"叔姻外祖父/叔姻外祖母","caller_o" : "令姻孫男","caller_s" : "舍姻孫男"}
daughter_niece={"caller":"女媳姻孫女","callee":"叔姻外祖父/叔姻外祖母","caller_o" : "令姻孫女","caller_s" : "舍姻孫女"}
daughter_nephew_o={"caller":"女媳姻外孫男","callee":"舅姻外祖父/舅姻外祖母","caller_o" : "令姻外孫男","caller_s" : "舍姻外孫男"}
daughter_niece_o={"caller":"女媳姻外孫女","callee":"舅姻外祖父/舅姻外祖母","caller_o" : "令姻外孫女","caller_s" : "舍姻外孫女"}

husband_father ={"caller":"婆公","callee":"兒婦/婦女","caller_o" : "令婆公","caller_s" : "家婆公"}
husband_mother ={"caller":"婆母","callee":"兒婦/婦女","caller_o" : "令婆母","caller_s" : "家婆母"}        
husband_brother_e = {"caller":"大伯","callee":"弟婦/弟妹","caller_o" : "令大伯","caller_s" : "家大伯"}
husband_brother_y = {"caller":"小叔","callee":"兄嫂/兄姊","caller_o" : "令小叔","caller_s" : "舍小叔"}
husband_brother_e_spouse = {"caller":"伯姆","callee":"叔姆","caller_o" : "令伯姆","caller_s" : "家大伯姆"}
husband_brother_y_spouse = {"caller":"叔姆","callee":"伯姆","caller_o" : "令叔姆","caller_s" : "舍小叔姆"}
husband_sister_e = {"caller":"大姑","callee":"兄婦/兄姊","caller_o" : "令大姑","caller_s" : "家大姑"}
husband_sister_y = {"caller":"小姑","callee":"弟婦/弟妹","caller_o" : "令大姑","caller_s" : "舍小姑"}
husband_sister_e_spouse = {"caller":"大姑夫","callee":"小舅姆/小舅媳婦/小舅弟婦/小舅婦/小妗子/小妗兒","caller_o" : "令大姑夫","caller_s" : "家大姑夫"}
husband_sister_y_spouse = {"caller":"小姑夫","callee":"大舅姆/大舅媳婦/大舅兄婦/大舅婦/大妗子/大妗兒","caller_o" : "令小姑夫","caller_s" : "舍小姑夫"}
husband_nephew = {"caller":"侄男","callee":"叔母/伯母","caller_o" : "令侄男","caller_s" : "舍侄男"}
husband_niece = {"caller":"侄女","callee":"叔母/伯母 ","caller_o" : "令侄女","caller_s" : "舍侄女"}
husband_nephew_o = {"caller":"甥男","callee":"舅母/妗母 ","caller_o" : "令甥男","caller_s" : "舍甥男"}
husband_niece_o = {"caller":"甥女","callee":"舅母/妗母","caller_o" : "令甥女","caller_s" : "舍甥女"}
husband_son = {"caller":"繼男","callee":"繼母/後母","caller_o" : "令堂","caller_s" : "家母"}
husband_daughter = {"caller":"繼女","callee":"繼母/後母","caller_o" : "令堂","caller_s" : "家母"}
husband_grandpa={"caller":"祖公","callee":"孫婦/孫媳婦","caller_o" : "令祖公","caller_s" : "家祖翁"}
husband_grandma ={"caller":"祖婆","callee":"孫婦/孫媳婦","caller_o" : "令祖婆","caller_s" : "家祖媼"} 
husband_grandpa_o={"caller":"外祖公","callee":"外孫婦/外孫媳婦","caller_o" : "令外祖公","caller_s" : "家外祖翁"}
husband_grandma_o={"caller":"外祖婆","callee":"外孫婦/外孫媳婦","caller_o" : "令外祖婆","caller_s" : "家外祖媼"} 
husband_uncle_e={"caller":"伯公","callee":"侄婦/侄媳婦","caller_o" : "令伯公","caller_s" : "家伯公"}
husband_uncle_y={"caller":"叔公","callee":"侄婦/侄媳婦","caller_o" : "令叔公","caller_s" : "家叔公"} 
husband_aunt_e={"caller":"伯婆","callee":"婆婆侄婦/婆婆侄媳婦","caller_o" : "令伯婆","caller_s" : "家伯婆"}
husband_aunt_y={"caller":"叔婆","callee":"婆婆侄婦/婆婆侄媳婦","caller_o" : "令叔婆","caller_s" : "家叔婆"}
husband_grandaunt ={"caller":"姑婆","callee":"侄婦/侄媳婦","caller_o" : "令姑婆","caller_s" : "家姑婆"}
husband_granduncle ={"caller":"姑公","callee":"内侄婦/丈人侄媳婦","caller_o" : "令姑公","caller_s" : "家姑公"}
husband_grandaunt_oe ={"caller":"舅婆","callee":"婆婆甥婦/婆婆甥媳婦","caller_o" : "令舅婆","caller_s" : "家舅婆"}
husband_granduncle_oe ={"caller":"舅公","callee":"甥婦/甥媳婦","caller_o" : "令舅公","caller_s" : "家舅公"}
husband_grandaunt_oy ={"caller":"姨婆","callee":"甥婦/甥媳婦","caller_o" : "令姨婆","caller_s" : "家姨婆"}
husband_granduncle_oy ={"caller":"姨公","callee":"内甥婦/丈人甥媳婦","caller_o" : "令姨公","caller_s" : "家姨公"}

wife_father ={"caller":"丈父","callee":"兒婿/婿男","caller_o" : "令尊岳","caller_s" : "家岳父"}
wife_mother ={"caller":"丈母","callee":"兒婿/婿男","caller_o" : "令岳母","caller_s" : "家岳母"}        
wife_brother_e = {"caller":"大舅","callee":"妹夫/妹兄","caller_o" : "令大舅","caller_s" : "家大舅"}
wife_brother_y = {"caller":"小舅","callee":"姊夫/姊弟","caller_o" : "令小舅","caller_s" : "舍小舅"}
wife_brother_e_spouse = {"caller":"舅姆","callee":"小姑夫","caller_o" : "令舅姆","caller_s" : "家大舅姆"}
wife_brother_y_spouse = {"caller":"舅姆","callee":"大姑夫","caller_o" : "令舅姆","caller_s" : "舍小舅姆"}
wife_sister_e = {"caller":"大姨","callee":"妹夫/妹兄","caller_o" : "令大姨","caller_s" : "家大姨"}
wife_sister_y = {"caller":"小姨","callee":"姊夫/姊弟","caller_o" : "令大姨","caller_s" : "舍小姨"}
wife_sister_e_spouse = {"caller":"大姨夫","callee":"小姨子女婿/小姨妹夫/小姨夫/婭/連襟弟","caller_o" : "令大姨夫","caller_s" : "家大姨夫"}
wife_sister_y_spouse = {"caller":"小姨夫","callee":"大姨子女婿/大姨姊夫/大姨夫/婭/連襟兄","caller_o" : "令小姨夫","caller_s" : "舍小姨夫"}
wife_nephew = {"caller":"侄男","callee":"姑父","caller_o" : "令侄男","caller_s" : "舍侄男"}
wife_niece = {"caller":"侄女","callee":"姑父 ","caller_o" : "令侄女","caller_s" : "舍侄女"}
wife_nephew_o = {"caller":"甥男","callee":"姨父 ","caller_o" : "令甥男","caller_s" : "舍甥男"}
wife_niece_o = {"caller":"甥女","callee":"姨父","caller_o" : "令甥女","caller_s" : "舍甥女"}
wife_son = {"caller":"繼男","callee":"繼父/後父","caller_o" : "令尊","caller_s" : "家父"}
wife_daughter = {"caller":"繼女","callee":"繼父/後父","caller_o" : "令尊","caller_s" : "家父"}
wife_grandpa={"caller":"祖丈人","callee":"孫婿/孫女婿","caller_o" : "令祖丈人","caller_s" : "家祖丈人"}
wife_grandma ={"caller":"祖丈母娘","callee":"孫婿/孫女婿","caller_o" : "令祖丈母娘","caller_s" : "家丈母"} 
wife_grandpa_o={"caller":"外祖丈人","callee":"外孫婿/外孫女婿","caller_o" : "令外祖丈人","caller_s" : "家外祖丈人"}
wife_grandma_o={"caller":"外祖丈母娘","callee":"外孫婿/外孫女婿","caller_o" : "令外祖丈母娘","caller_s" : "家外祖丈母"} 
wife_uncle_e={"caller":"伯丈人","callee":"侄婿/侄女婿","caller_o" : "令伯丈人","caller_s" : "家伯丈人"}
wife_uncle_y={"caller":"叔丈人","callee":"侄婿/侄女婿","caller_o" : "令叔丈人","caller_s" : "家叔丈人"} 
wife_aunt_e={"caller":"伯丈母","callee":"婆婆侄婿/婆婆侄女婿","caller_o" : "令伯丈母娘","caller_s" : "家伯丈母娘"}
wife_aunt_y={"caller":"叔丈母","callee":"婆婆侄婿/婆婆侄女婿","caller_o" : "令叔丈母娘","caller_s" : "家叔丈母娘"}
wife_grandaunt ={"caller":"姑丈母","callee":"侄婿/侄女婿","caller_o" : "令姑丈母","caller_s" : "家姑丈母"}
wife_granduncle ={"caller":"姑丈人","callee":"内侄女婿/丈人侄女婿","caller_o" : "令姑丈人","caller_s" : "家姑丈人"}
wife_grandaunt_oe ={"caller":"舅丈母","callee":"婆婆甥女婿","caller_o" : "令舅丈母","caller_s" : "家舅丈母"}
wife_granduncle_oe ={"caller":"舅丈人","callee":"甥婿/甥女婿","caller_o" : "令舅丈人","caller_s" : "家舅丈人"}
wife_grandaunt_oy ={"caller":"姨丈母","callee":"甥婿/甥女婿","caller_o" : "令姨丈母","caller_s" : "家姨丈母"}
wife_granduncle_oy ={"caller":"姨丈人","callee":"内甥女婿/丈人甥女婿","caller_o" : "令姨丈人","caller_s" : "家姨丈人"}

grand={
	"祖":"在古代，廣義是指所有父輩以上的男性先輩，狹義則是指祖父。",
    "祖父":"又稱為「王父」、「大父」、「祖君」。在古代，「公」、「太公」、「翁」也可用來稱呼祖父；如今對祖父最常見的稱呼是「爺爺」。",
    "祖母":"又可以稱為「大母」、「王母」、 「重慈」。又因古人有妻有妾，所以祖母又有 「季祖母」、「庶祖母」、「妾祖母」之分。祖母之稱古今通用。",
    "婆":"是古代對成年婦女的很普遍的稱呼，也可以用來稱祖母。",
    "奶奶":"是今天對祖母的普遍稱呼，古代的使用較晚。作為稱謂，「奶」最早是作為乳母之稱，以後又用以稱母親，又作為對以婚婦女的較廣義的稱呼。",
    "堂祖父":"對祖父的兄弟的稱謂",
    "堂祖母":"對祖父兄弟妻子的稱謂。",
	"曾祖":"即祖父之父。古代還有「太翁」、「曾翁」、「曾大父」、「大王父」、「王大父」、「太公」、「曾太公」等稱呼，比較特殊的是稱「曾門」。",
    "曾祖母":"指曾祖之妻，還可以稱為「太婆」、「曾祖王母」、「太奶」，其中較常見的為「太婆」",
	"高祖":"即曾祖之父，古今多稱為高祖父，也有稱為「高祖王父」、「高門」。但需注意的是，古代對高祖之上的歷代遠祖也可稱為高祖。",
    "高祖母":"指高祖之妻，或稱「高王祖母」。"
}

parent={
	"父母":"父母是親屬中最重要的親屬，除「父母」、「雙親」、「二老」、「爹娘」等古今通用的合稱外還有「高堂」、「嚴君」、「尊親」、「嚴親」、「兩親」、「親闈」等以及文人筆下的「所生」、「椿萱」等對父母的代稱。",
    "父":"是對父親古今習見的稱呼，還可以稱父親為「公」、「翁」、「尊」、「大人」、「嚴君」、「爺」、「爹」、「爸」、「老子」等。",
    "尊":"古代常見的敬稱用語，稱自己的父親可稱「家尊」，稱對方的父親則稱「令尊」。",
    "爺":"古代對成年男子較廣義的稱呼，宋代開始用作對祖父之稱，魏晉南北朝就用作對父親之稱，或寫作「耶」。",
    "母":"是對母親最常見的稱呼。而在古代對母親的稱謂中，大都和「母」相似，又用作對成年婦女或老年婦女的泛稱。其中較重要的有：「婆」、「娘」、「娘娘」、「姥」、「大人」、「媽」、「慈」、「家家」和「姊姊」等。",
    "繼母":"如果自己的母親去世、離異或被父輩逐出，則稱續娶之妻為繼母、繼親、後母、假母、續母。",
    "出母":"如果自己的母親離家之後還能相見，則稱為出母。",
    "生母":"在古代一夫多妻制的家庭中，稱自己的生身母親為「生母」或 「本生母」。",
    "庶母":"在古代一夫多妻制的家庭中，如果自己的生母是正妻，則稱父親之妾為「庶母」、「少母」、「諸母」、「妾母」。",
    "家家":"是中古時期對母親的一種特殊稱呼。",
    "姊姊":"是中古時期對母親的一種特殊稱呼。",
    "姨":"在古代一夫多妻制的家庭中，無論自己的生母是妻或妾，對父親的妾都可以稱為「姨」、「姨姨」、「阿姨」。",
    "義父":"指是在自己的父親之外再拜認某人為父，這個「義」字有外加、假、代、自願等意。",
    "義母":"指是在自己的母親之外再拜認某人為母。",
    "考":"考只用來對死去的父親之稱，死去的祖輩乃至更早的直系先輩均可用考妣相稱",
    "妣":"妣只用來對死去的母親之稱，死去的祖輩乃至更早的直系先輩均可用考妣相稱"
}

married_couple={
	"夫":"或作「丈夫」，本是對成年男子的美稱，但又用作夫妻之夫。「夫」加上其它附加成分的表示丈夫意的相關稱謂很多，如：「夫子」、「夫君」、「夫主」、「夫婿」等。除此，還可以用「良人」 、「郎」、「丈人」、「君」、「老公」、「官人」、「漢子」等稱呼丈夫。",
    "妻":"是由古至今對妻的最主要的稱呼。在妻之前加上各種附加成分，還有「賢妻」、「良妻」、「仁妻」、「令妻」、「嬌妻」等。除此，還可用「婦」、「室」、「君」、「夫人」、「娘子」、「渾家」、「內」、「老婆」、「婆娘」、「太太」等來稱呼。"
}

parent_rel_honor={
	"諸父":"是對父親的兄弟的統稱。 ",
    "諸母":"是對父親的妻室的統稱。",
    "世父":"對父親的兄弟的稱謂，現在更多的場合是稱「伯父」、「叔父」或簡稱「伯」、「叔」。古人偶爾將幾個叔父按伯、仲、叔、季的排行次序，分別稱為「伯父」、「仲父」、「叔父」、「季父」。",
    "伯母":"是對父親的兄長的妻室的稱呼。",
    "叔母":"是對父親的弟弟的妻室的稱呼。",
    "從父":"對父親的叔伯兄弟可統稱「從父」，又可分別稱為「從伯」、「從叔」。",
    "姑":"對父親的姊妹可稱為「姑」（沿用至今），又可以稱為「諸姑」、「姑姊」、「姑妹」，對已婚者一般都稱為「姑母」、「姑媽」，與今不同的是偶爾也稱「姑娘」。",
    "姑父":"對姑母的丈夫，既可稱為「姑父」、「姑丈」，又可以稱為「姑婿」、「姑夫」。",
    "表兄弟":"對姑母的子的稱謂。",
    "表姊妹":"對姑母的女的稱謂。",
	"外祖父":"對母親的父親，稱其為「外祖父」（與今同），又可稱為「外翁」、「外大人」、「家公」、「老爺」等。",
    "外祖母":"對母親的母親，稱為「外祖母」、「外婆」（與今同），又稱為「姥姥」、「老老」等。",
    "舅":"對母親的兄弟，古今均稱「舅」，在不同場合，可加上一些修飾或補充性文字，如：「舅氏」、「舅父」、「嫡舅」、「元舅」、「堂舅」等。",
    "舅母":"又分「大舅母」（大妗子）、「小舅母」（小妗子）是對舅父之妻的稱謂。",
    "姨母":"對母親姊妹的稱呼，先秦時稱為「從母」，秦漢以來則稱為「姨母」，或稱為「姨娘」、「姨婆」、「姨媽」等。",
    "姨父":"對姨母之夫稱為「姨夫」或「姨父」。姨母之子女也稱「表兄弟」、「表姊妹」。（無論是舅父之女、姨母之女，還是姑母之女，都可以以「表兄弟」、「表姊妹」相稱，古人統稱為「諸表」。）"
}

mc_rel_honor={
	"公":"也稱公公，對丈夫之父，古稱為「舅」，也稱為「公」、「公公 」。這些稱呼正是今天稱丈夫之父為「公」、「公公」、「老人公」的前身。",
    "婆":"也稱婆婆，對丈夫之母，古稱為「姑」以及由「姑」派生出的「君姑」、「嚴姑」、「慈姑」、「阿姑」等。後又稱「婆」、「婆婆」。",
    "舅姑":"是早期對丈夫父母的合稱。近者稱「公婆」。此外還有一個常見的稱呼是「姑章」，或作「姑嫜」。",
    "姑舅":"是早期對丈夫父母的合稱。近者稱「公婆」。此外還有一個常見的稱呼是「姑章」，或作「姑嫜」。",
    "伯叔":"對丈夫的兄弟的稱謂，與近代所稱的「大伯子」（大伯）、「小叔子」（小叔）是一致的",
    "姑子":"對丈夫的姐姐或妹妹的稱謂，或稱「大姑子」（夫姑）、「小姑子」（小姑）。",
	"岳丈":"是對於妻子之父的稱呼，古代還有「泰山」、「冰翁」 外舅」 「外父」、「妻父」等代稱。",
    "岳母":"對妻子之母的稱謂，或稱為「丈母」、「丈母娘」。",
    "姑":"早期用來對妻子之母的稱呼。",
    "外姑":"早期用來對妻子之母的稱呼。",
    "舅舅":"對妻子兄弟的稱呼，或稱為「舅」、「舅爺」、「舅子」、「大舅子」、「小舅子」等，還稱為「內兄」、「內弟」、「妻兄」、「妻弟」等。",
    "姨":"對妻子的姐姐或姊妹的稱呼，或稱「大姨子」（大姨）、「小姨子」（小姨），也稱為「妻妹」、「內妹」。"
}

brother_honor={
	"兄":"又稱為「昆」。今天則可用「哥」來稱呼兄長。有兄弟數人的情況下，稱呼中必須表示出排行，或以數字為排行，或用伯、仲、叔、季這些排行常用語等。（「哥」，古代是用得十分廣泛的稱呼，可以稱父、稱兄、稱弟、稱子。）",
    "嫂":"對兄的妻子的稱謂，或稱「嫂嫂」。",
    "弟":"是對與兄相對者的稱呼。",
    "弟媳":"對弟的妻子的稱謂，或稱「弟妹」。",
    "侄":"對兄弟的子女最常見的稱呼，也可直接稱之為「兄子」、「兄女」，或稱為「從子」、「從女」、「猶子」、「猶女」。"
}

sister_honor={
	"女兄":"古代對姊妹的稱謂，或直接稱姊妹為兄弟。「姊」又稱「姐」，與姊相對者稱為「妹」。",
    "女弟":"古代對姊妹的稱謂，或直接稱姊妹為兄弟。「姊」又稱「姐」，與姊相對者稱為「妹」。",
    "姊夫":"對姊姊的丈夫的稱呼，也可稱為「姊婿」、「妹婿」。",
    "妹夫":"對妹妹的丈夫的稱呼，也可稱為「姊婿」、「妹婿」。",
    "甥":"對姊妹之子最普遍的稱呼，還稱為「外甥」、「甥女」、「外甥女」。"
}

child_honor={
	"子":"古代是一個使用範圍較廣的稱呼，秦漢以後主要用作兒子之稱。自己之子可稱為「犬子」、「孽子」、「不孝子」等，別人之子又可稱為「令子」、「良子」、「不凡子」、「賢子」等。除此，還可用「男」、「子息」、「賤息」、「兒子」、「兒郎」、「兒男」等來稱呼子。若有幾個兒子則有「長子」、「次男」、「幼子」等稱呼。",
    "女":"對女兒的主要稱呼。對別人的女兒往往稱為「愛」或「嬡」，也稱為「令嬡」、「閨嬡」。",
    "義子":"指不是自己生育的，而是收養的兒子，又稱「養子」、「假子」。同時還有一個常見的代稱「螟蛉」。",
    "義女":"指不是自己生育的，而是收養的女兒，又稱「養女」、「假子」。同時還有一個常見的代稱「螟蛉」。",
    "媳婦":"對兒子之妻的稱呼。最初只稱為「婦」，後因兒子又稱為「息」，所以子之妻又稱為「息婦」，或寫作「媳婦」。",
    "婿":"對女兒丈夫的稱呼，或稱為「女婿」、「子婿」、「郎婿」、「快婿」等。除此，女兒之夫還可以被稱為「女夫」、「半子」、「東床」「令坦」。女婿到了岳丈家，除了岳父、岳母可以稱「賢婿」之類，岳家一般人都尊稱其為「姑爺」、「姑老爺」。",
    "孫":"是對兒子的兒子或是兒子的女兒的稱呼，或稱「孫息」、「孫枝」。「孫」又分為「孫兒」、「孫子」、「孫女」；孫女又稱為「女孫」。",
    "外孫":"對女兒的子女的稱呼。女姓還可稱為「外孫女」。"
}


father = {
    "父親":father_father,
    "母親":father_mother,
    "哥哥":father_brother_e,
    "弟弟":father_brother_y,
    "兄婦":father_brother_e_spouse,
    "弟婦":father_brother_y_spouse,
    "姊姊":father_sister_e,
    "妹妹":father_sister_y,
    "姊夫":father_sister_e_spouse,
    "妹夫":father_sister_y_spouse,
    "侄男":father_nephew,
    "侄女":father_niece,
    "甥男":father_nephew_o,
    "甥女":father_niece_o,
    "男兒":father_son,
    "女兒":father_daughter,
    "祖父":father_grandpa,
    "祖母":father_grandma,
    "外祖父":father_grandpa_o,
    "外祖母":father_grandma_o,
    "伯父":father_uncle_e,
    "叔父":father_uncle_y,
    "伯母":father_aunt_e,
    "叔母":father_aunt_y,
    "姑母":father_grandaunt,
    "姑父":father_granduncle,
    "舅父":father_granduncle_oe,
    "舅母":father_grandaunt_oe,
    "姨父":father_granduncle_oy,
    "姨母":father_grandaunt_oy
}

mother = {
    "父親":mother_father,
    "母親":mother_mother,
    "哥哥":mother_brother_e,
    "弟弟":mother_brother_y,
    "兄婦":mother_brother_e_spouse,
    "弟婦":mother_brother_y_spouse,
    "姊姊":mother_sister_e,
    "妹妹":mother_sister_y,
    "姊夫":mother_sister_e_spouse,
    "妹夫":mother_sister_y_spouse,
    "侄男":mother_nephew,
    "侄女":mother_niece,
    "甥男":mother_nephew_o,
    "甥女":mother_niece_o,
    "男兒":mother_son,
    "女兒":mother_daughter,
    "祖父":mother_grandpa,
    "祖母":mother_grandma,
    "外祖父":mother_grandpa_o,
    "外祖母":mother_grandma_o,
    "伯父":mother_uncle_e,
    "叔父":mother_uncle_y,
    "伯母":mother_aunt_e,
    "叔母":mother_aunt_y,
    "姑母":mother_grandaunt,
    "姑父":mother_granduncle,
    "舅父":mother_granduncle_oe,
    "舅母":mother_grandaunt_oe,
    "姨父":mother_granduncle_oy,
    "姨母":mother_grandaunt_oy
}

brother_e = {
    "妻子":brother_e_spouse,
    "男兒":brother_son,
    "女兒":brother_daughter,
    "兒婦":brother_daughter_in_law,
    "兒婿":brother_son_in_law,
    "孫男兒":brother_grandson,
    "孫女兒":brother_granddaughter,
    "外孫男兒":brother_grandson_o,
    "外孫女兒":brother_granddaughter_o,
    "丈人":brother_e_father_in_law,
    "丈母娘":brother_e_mother_in_law,
    "大舅子":brother_e_brother_in_law_e,
    "小舅子":brother_e_brother_in_law_y,
    "大姨子":brother_e_sister_in_law_e,
    "小姨子":brother_e_sister_in_law_y,
    "大吟子":brother_e_brother_e_spouse,
    "小吟子":brother_e_brother_y_spouse,
    "大姨夫":brother_e_sister_e_spouse,
    "小姨夫":brother_e_sister_y_spouse,
    "内侄男":brother_e_nephew,
    "内侄女":brother_e_niece,
    "内甥男":brother_e_nephew_o,
    "内甥女":brother_e_niece_o
}

brother_y = {
    "妻子":brother_y_spouse,
    "男兒":brother_son,
    "女兒":brother_daughter,
    "兒婦":brother_daughter_in_law,
    "兒婿":brother_son_in_law,
    "孫男兒":brother_grandson,
    "孫女兒":brother_granddaughter,
    "外孫男兒":brother_grandson_o,
    "外孫女兒":brother_granddaughter_o,
    "丈人":brother_y_father_in_law,
    "丈母娘":brother_y_mother_in_law,
    "大舅子":brother_y_brother_in_law_e,
    "小舅子":brother_y_brother_in_law_y,
    "大姨子":brother_y_sister_in_law_e,
    "小姨子":brother_y_sister_in_law_y,
    "大吟子":brother_y_brother_e_spouse,
    "小吟子":brother_y_brother_y_spouse,
    "大姨夫":brother_y_sister_e_spouse,
    "小姨夫":brother_y_sister_y_spouse,
    "内侄男":brother_y_nephew,
    "内侄女":brother_y_niece,
    "内甥男":brother_y_nephew_o,
    "内甥女":brother_y_niece_o
    }

sister_e = {
    "丈夫":sister_e_spouse,
    "男兒":sister_son,
    "女兒":sister_daughter,
    "兒婦":sister_daughter_in_law,
    "兒婿":sister_son_in_law,
    "孫男兒":sister_grandson,
    "孫女兒":sister_granddaughter,
    "外孫男兒":sister_grandson_o,
    "外孫女兒":sister_granddaughter_o,
    "丈人":sister_e_father_in_law,
    "丈母娘":sister_e_mother_in_law,
    "大舅子":sister_e_brother_in_law_e,
    "小舅子":sister_e_brother_in_law_y,
    "大姨子":sister_e_sister_in_law_e,
    "小姨子":sister_e_sister_in_law_y,
    "大吟子":sister_e_brother_e_spouse,
    "小吟子":sister_e_brother_y_spouse,
    "大姨夫":sister_e_sister_e_spouse,
    "小姨夫":sister_e_sister_y_spouse,
    "夫侄男":sister_e_nephew,
    "夫侄女":sister_e_niece,
    "夫甥男":sister_e_nephew_o,
    "夫甥女":sister_e_niece_o
}

sister_y = {
    "丈夫":sister_y_spouse,
    "男兒":sister_son,
    "女兒":sister_daughter,
    "兒婦":sister_daughter_in_law,
    "兒婿":sister_son_in_law,
    "孫男兒":sister_grandson,
    "孫女兒":sister_granddaughter,
    "外孫男兒":sister_grandson_o,
    "外孫女兒":sister_granddaughter_o,
    "丈人":sister_y_father_in_law,
    "丈母娘":sister_y_mother_in_law,
    "大舅子":sister_y_brother_in_law_e,
    "小舅子":sister_y_brother_in_law_y,
    "大姨子":sister_y_sister_in_law_e,
    "小姨子":sister_y_sister_in_law_y,
    "大吟子":sister_y_brother_e_spouse,
    "小吟子":sister_y_brother_y_spouse,
    "大姨夫":sister_y_sister_e_spouse,
    "小姨夫":sister_y_sister_y_spouse,
    "夫侄男":sister_y_nephew,
    "夫侄女":sister_y_niece,
    "夫甥男":sister_y_nephew_o,
    "夫甥女":sister_y_niece_o
    }

son = {
    "妻子":son_spouse,
    "男兒":son_son,
    "女兒":son_daughter,
    "兒婦":son_daughter_in_law,
    "兒婿":son_son_in_law,
    "孫男兒":son_grandson,
    "孫女兒":son_granddaughter,
    "外孫男兒":son_grandson_o,
    "外孫女兒":son_granddaughter_o,
    "丈人":son_father_in_law,
    "丈母娘":son_mother_in_law,
    "大舅子":son_brother_in_law_e,
    "小舅子":son_brother_in_law_y,
    "大姨子":son_sister_in_law_e,
    "小姨子":son_sister_in_law_y,
    "大吟子":son_brother_e_spouse,
    "小吟子":son_brother_y_spouse,
    "大姨夫":son_sister_e_spouse,
    "小姨夫":son_sister_y_spouse,
    "内侄男":son_nephew,
    "内侄女":son_niece,
    "内甥男":son_nephew_o,
    "内甥女":son_niece_o
}

daughter = {
    "丈夫":daughter_spouse,
    "男兒":daughter_son,
    "女兒":daughter_daughter,
    "兒婦":daughter_daughter_in_law,
    "兒婿":daughter_daughter_in_law,
    "孫男兒":daughter_grandson,
    "孫女兒":daughter_granddaughter,
    "外孫男兒":daughter_granddaughter_o,
    "外孫女兒":daughter_granddaughter_o,
    "丈人":daughter_father_in_law,
    "丈母娘":daughter_mother_in_law,
    "大舅子":daughter_brother_in_law_e,
    "小舅子":daughter_brother_in_law_y,
    "大姨子":daughter_sister_in_law_e,
    "小姨子":daughter_sister_in_law_y,
    "大吟子":daughter_brother_e_spouse,
    "小吟子":daughter_brother_y_spouse,
    "大姨夫":daughter_sister_e_spouse,
    "小姨夫":daughter_sister_y_spouse,
    "内侄男":daughter_nephew,
    "内侄女":daughter_niece,
    "内甥男":daughter_nephew_o,
    "内甥女":daughter_niece_o
}

husband = {
    "父親":husband_father,
    "母親":husband_mother,
    "哥哥":husband_brother_e,
    "弟弟":husband_brother_y,
    "兄婦":husband_brother_e_spouse,
    "弟婦":husband_brother_y_spouse,
    "姊姊":husband_sister_e,
    "妹妹":husband_sister_y,
    "姊夫":husband_sister_e_spouse,
    "妹夫":husband_sister_y_spouse,
    "侄男":husband_nephew,
    "侄女":husband_niece,
    "甥男":husband_nephew_o,
    "甥女":husband_niece_o,
    "男兒":husband_son,
    "女兒":husband_daughter,
    "祖父":husband_grandpa,
    "祖母":husband_grandma,
    "外祖父":husband_grandpa_o,
    "外祖母":husband_grandma_o,
    "伯父":husband_uncle_e,
    "叔父":husband_uncle_y,
    "伯母":husband_aunt_e,
    "叔母":husband_aunt_y,
    "姑母":husband_grandaunt,
    "姑父":husband_granduncle,
    "舅父":husband_granduncle_oe,
    "舅母":husband_grandaunt_oe,
    "姨父":husband_granduncle_oy,
    "姨母":husband_grandaunt_oy
}

wife = {
    "父親":wife_father,
    "母親":wife_mother,
    "哥哥":wife_brother_e,
    "弟弟":wife_brother_y,
    "兄婦":wife_brother_e_spouse,
    "弟婦":wife_brother_y_spouse,
    "姊姊":wife_sister_e,
    "妹妹":wife_sister_y,
    "姊夫":wife_sister_e_spouse,
    "妹夫":wife_sister_y_spouse,
    "侄男":wife_nephew,
    "侄女":wife_niece,
    "甥男":wife_nephew_o,
    "甥女":wife_niece_o,
    "男兒":wife_son,
    "女兒":wife_daughter,
    "祖父":wife_grandpa,
    "祖母":wife_grandma,
    "外祖父":wife_grandpa_o,
    "外祖母":wife_grandma_o,
    "伯父":wife_uncle_e,
    "叔父":wife_uncle_y,
    "伯母":wife_aunt_e,
    "叔母":wife_aunt_y,
    "姑母":wife_grandaunt,
    "姑父":wife_granduncle,
    "舅父":wife_granduncle_oe,
    "舅母":wife_grandaunt_oe,
    "姨父":wife_granduncle_oy,
    "姨母":wife_grandaunt_oy
}

honor = {
    "祖輩":grand,
    "父母":parent,
    "夫妻":married_couple,
    "父母親戚":parent_rel_honor,
    "夫妻親戚":mc_rel_honor,
    "兄弟":brother_honor,
    "姊妹":sister_honor,
    "子女":child_honor
}

list_rel=["父親","母親","哥哥","弟弟","姊姊","妹妹","男兒","女兒","丈夫","妻子"]

def relative_name(str):
    if str[0:2]=="父親":
        if father.get(str[3:],"未知")!="未知":
            return (name_info(father.get(str[3:])))
        else:
            return key_info(father,str)
    elif str[0:2]=="母親":
        if mother.get(str[3:],"未知")!="未知":
            return (name_info(mother.get(str[3:])))
        else:
            return key_info(mother,str)
    elif str[0:2]=="哥哥":
        if brother_e.get(str[3:],"未知")!="未知":
            return (name_info(brother_e.get(str[3:])))
        else:
            return key_info(brother_e,str)
    elif str[0:2]=="弟弟":
        if brother_y.get(str[3:],"未知")!="未知":
            return (name_info(brother_y.get(str[3:])))
        else:
            return key_info(brother_y,str)
    elif str[0:2]=="姊姊":
        if sister_e.get(str[3:],"未知")!="未知":
            return (name_info(sister_e.get(str[3:])))
        else:
            return key_info(brother_e,str)
    elif str[0:2]=="妹妹":
        if sister_y.get(str[3:],"未知")!="未知":
            return (name_info(sister_y.get(str[3:])))
        else:
            return key_info(sister_y,str)
    elif str[0:2]=="男兒":
        if son.get(str[3:],"未知")!="未知":
            return (name_info(son.get(str[3:])))
        else:
            return key_info(son,str)
    elif str[0:2]=="女兒":
        if daughter.get(str[3:],"未知")!="未知":
            return (name_info(daughter.get(str[3:])))
        else:
            return key_info(daughter,str)
    elif str[0:2]=="丈夫":
        if husband.get(str[3:],"未知")!="未知":
            return (name_info(husband.get(str[3:])))
        else:
            return key_info(husband,str)
    elif str[0:2]=="妻子":
        if wife.get(str[3:],"未知")!="未知":
            return (name_info(wife.get(str[3:])))
        else:
            return key_info(wife,str)
    else:
        pass

def honor_list_exist(str,key):
    if str in honor:
        if key in honor.get(str):
            return True
    return False

def honor_list_info(str):
    strm=str
    if len(str)==4:
        strm = str[0:2]+"的"+str[2:4]
    info = "對於\""+strm+"\"可查詢:"
    for k in honor.get(str).keys():
        info = info +"\n\t"+ k
    return info    

def honor_info(str,key):
    if str in honor:
        if key in honor.get(str):
            return honor.get(str).get(key)
    return False
                       
def name_info(d):
    return("稱呼(稱謂): "+d["caller"]+"\n自稱: "+d["callee"]+"\n對他人稱其家族中人: "+d["caller_o"]+"\n對他人稱自己家族中人: "+d["caller_s"])

def key_info(d,str):
    info = "未知,對於\""+str[0:2]+"的”可提供:"
    for k in d.keys():
        info = info +"\n\t"+ k
    return info

def list_info():
    info = "可供查詢的一等親包含："
    for k in list_rel:
        info = info +"\n\t"+ k
    return info