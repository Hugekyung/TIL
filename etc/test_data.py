import pandas as pd
import re

x = """ _happiness_o         |
| _imyour_joy          |
| _mariahwasa          |
| _seorina             |
| 216jung              |
| 2xj_hee              |
| 515sunnyday          |
| ahnhani_92           |
| ara_go_0211          |
| ayeoniiiiii          |
| ch_amii              |
| clean_0828           |
| d_a___m_i            |
| dahee0315            |
| dancingmulgogi       |
| daraxxi              |
| dlgofl85             |
| dlwlrma              |
| doflwl               |
| doonabae             |
| e.jiah               |
| esom_                |
| eugene810303         |
| gagkimminkyoung      |
| geewonii             |
| gominsi              |
| goyounjung           |
| greentee.park        |
| han_bling_           |
| han_ye_seul_         |
| hanhyojoo222         |
| hatfelt              |
| hehehe0              |
| heizeheize           |
| hellobeen            |
| hellopapa11          |
| heybiblee            |
| hi_sseulgi           |
| hongsuzu             |
| hoyatoya             |
| hs_kim_95            |
| hv_nara              |
| hye_yoon1110         |
| hyeri_0609           |
| hyoyeon_x_x          |
| hyunah_aa            |
| hyuniiiiiii_95917    |
| i_icaruswalks        |
| iammingki            |
| illusomina           |
| iluvyub              |
| im_hyeonzzu          |
| itzy.all.in.us       |
| j_chaeyeoni          |
| j0i3n2a9             |
| jang.doyoun          |
| jennierubyjane       |
| jeon.yeobeen         |
| jeongeuiyam          |
| jessicah_o           |
| jh_han               |
| jihye8024            |
| jihyesharp           |
| jinjoo1224           |
| jinkijoo             |
| jiyeon2__            |
| jsomin86             |
| jung.sia             |
| junghyesung91        |
| k_hanna_             |
| kieunse              |
| kimjihye79           |
| kimtaeri_official    |
| kosoyoung_official   |
| kyo1122              |
| lalalalisa_m         |
| lavieenbluu          |
| lee.hyunyi           |
| leechungah           |
| leehi_hi             |
| leejin_321           |
| leesiyoung38         |
| lovely.katie.k       |
| luv_ribbon           |
| m_kayoung            |
| marcellasne_         |
| minah320_97          |
| miyayeah             |
| mo_onbyul            |
| modelhanhyejin       |
| nayoung_lim95        |
| nayoungkeem          |
| o._.julia            |
| ohvely22             |
| pinkeh2015           |
| rachel_mypark        |
| roma.emo             |
| ron_sae              |
| roses_are_rosie      |
| rovvxhyo             |
| ryuniverse328        |
| seojuhyun_s          |
| shindandan_          |
| sjkuksee             |
| skuukzky             |
| sodam_park_0908      |
| somin_jj             |
| somsomi0309          |
| soobinms             |
| sooyaaa__            |
| sooyoungchoi         |
| ssoheean             |
| ssoyang84            |
| ssung916             |
| stephanielee199      |
| summer.jeong         |
| sunbin_eyemag        |
| sung_yuri_           |
| sunye.m              |
| susemee              |
| sysysy1102           |
| taeyeon_ss           |
| thousand_wooo        |
| tiffanyyoungofficial |
| todayis_wendy        |
| twin99yj             |
| wg_lim               |
| wow_kimsohyun        |
| xeesoxee             |
| xodambi              |
| xxadoraa             |
| ye._.vely618         |
| yebin__              |
| yejinhand            |
| yeo_jooha            |
| yerimiese            |
| yerin_the_genuine    |
| yjiinp               |
| yoanaloves           |
| yoonjujang           |
| you_r_love           |
| youngji_02           |
| yubi_190             |
| yulyulk              |
| yura_936             |
| z_hera               |
| ziyooni    """
x = re.sub('\n', '', x)
x = re.sub('[|]', '', x)
x = re.sub(' +', ' ', x)
x_list = list(x.split())
# print(x_list)

inf = pd.read_csv(r'D:/kmong/instagram_dashboard/influencer_re.csv')
inf_list = inf['username'].tolist()
inf_unique = pd.unique(inf_list)
# print(inf_list)

notid = []
for i in inf_list:
    if i not in x_list:
        # print(i)
        notid.append(i)
print("없는 아이디 리스트: ", notid) # db에 insert되지 않은 인스타 아이디