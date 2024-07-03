import tkinter as tk
from tkinter.messagebox import showwarning
import random
import numpy as np

def Variant(Number):


    if Number == 1:
        X1 = [[['3', '20', '12', '880'], ['24', '2', '17', '4828'], ['7', '6', '27', '1716'],['23', '18', '30','4920'], ['10', '9', '15', '2172']],
              [['3', '20', '12', '916'], ['24', '2', '17', '5116'], ['7', '6', '27', '1800'],['23', '18', '30', '5196'], ['21', '28', '29', '2292']],
              [['3', '20', '12', '925'], ['24', '2', '17', '5188'], ['7', '6', '27', '1821'],['23', '18', '30', '5265'], ['21', '28', '29', '2322']],
              [['3', '20', '12', '937'], ['24', '2', '17', '5284'], ['7', '6', '27', '1849'],['23', '18', '30', '5357'], ['21', '28', '29', '2362']],
              [['3', '20', '12', '913'], ['24', '2', '17', '5092'], ['7', '6', '27', '1793'],['23', '18', '30', '5173'], ['21', '28', '29', '2282']],
              [['3', '20', '12', '880'], ['24', '2', '17', '4828'], ['7', '6', '27', '1716'],['23', '18', '30', '4920'], ['21', '28', '29', '2172']]]
        return X1

    if Number == 2:
        X1 = [[['15', '21', '21', '3195'], ['17', '20', '30', '3634'], ['24', '19', '27', '4949'], ['30', '8', '29', '6027'], ['7', '21', '23', '1673']],
              [['15', '21', '21', '3390'], ['17', '20', '30', '3855'], ['24', '19', '27', '5261'], ['30', '8', '29', '6417'], ['7', '21', '23', '1764']],
              [['15', '21', '21', '3195'], ['17', '20', '30', '3634'], ['24', '19', '27', '4949'], ['30', '8', '29', '6027'], ['7', '21', '23', '1673']],
              [['15', '21', '21', '3360'], ['17', '20', '30', '3821'], ['24', '19', '27', '5213'], ['30', '8', '29', '6357'], ['7', '21', '23', '1750']],
              [['15', '21', '21', '3315'], ['17', '20', '30', '3770'], ['24', '19', '27', '5141'], ['30', '8', '29', '6267'], ['7', '21', '23', '1729']],
              [['15', '21', '21', '3300'], ['17', '20', '30', '3753'], ['24', '19', '27','5117'], ['30', '8', '29', '6237'], ['7', '21', '23', '1722']]]
        return X1

    if Number == 3:
        X1 = [[['8', '20', '22', '1756'], ['18', '16', '29', '3712'], ['19', '14', '14', '3807'],['23', '30', '21', '4685'], ['24', '17', '28', '4868']],
              [['8', '20', '22', '1748'], ['18', '16', '29', '3694'], ['19', '14', '14', '3788'],['23', '30', '21', '4662'], ['24', '17', '28', '4844']],
              [['8', '20', '22', '1836'], ['18', '16', '29', '3892'], ['19', '14', '14', '3997'],['23', '30', '21', '4915'], ['24', '17', '28', '5108']],
              [['8', '20', '22', '1748'], ['18', '16', '29', '3694'], ['19', '14', '14', '3788'],['23', '30', '21', '4662'], ['24', '17', '28', '4844']],
              [['8', '20', '22', '1852'], ['18', '16', '29', '3928'], ['19', '14', '14', '4035'],['23', '30', '21', '4961'], ['24', '17', '28', '5156']],
              [['8', '20', '22', '1884'], ['18', '16', '29', '4000'], ['19', '14', '14', '4111'],['23', '30', '21', '5053'], ['24', '17', '28', '5252']]]
        return X1

    if Number == 4:
        X1 = [[['2', '28', '12', '678'], ['9', '13', '21', '1996'], ['29', '16', '16', '5837'],['26', '25', '17', '5329'], ['16', '1', '20', '4367']],
              [['2', '28', '12', '676'], ['9', '13', '21', '1987'], ['29', '16', '16', '5808'],['26', '25', '17', '5303'], ['16', '1', '20', '4346']],
              [['2', '28', '12', '708'], ['9', '13', '21', '2131'], ['29', '16', '16', '6272'],['26', '25', '17', '5719'], ['16', '1', '20', '4430']],
              [['2', '28', '12', '678'], ['9', '13', '21', '1996'], ['29', '16', '16', '5837'],['26', '25', '17', '5329'], ['16', '1', '20', '4535']],
              [['2', '28', '12', '704'], ['9', '13', '21', '2113'], ['29', '16', '16', '6214'],['26', '25', '17', '5667'], ['16', '1', '20', '4829']],
              [['2', '28', '12', '710'], ['9', '13', '21', '2140'], ['29', '16', '16', '6301'],['26', '25', '17', '5745'], ['16', '1', '20', '4451']]]
        return X1

    if Number == 5:
        X1 = [[['18', '9', '6', '3600'], ['7', '6', '20', '1574'], ['5', '6', '19', '1237'],['13', '13', '5', '2645'], ['17', '2', '17', '3463']],
              [['18', '9', '6', '3564'], ['7', '6', '20', '1560'], ['5', '6', '19', '1227'],['13', '13', '5', '2619'], ['17', '2', '17', '3429']],
              [['18', '9', '6', '3762'], ['7', '6', '20', '1637'], ['5', '6', '19', '1282'],['13', '13', '5', '2762'], ['17', '2', '17', '3616']],
              [['18', '9', '6', '4104'], ['7', '6', '20', '1770'], ['5', '6', '19', '1377'],['13', '13', '5', '3009'], ['17', '2', '17', '3939']],
              [['18', '9', '6', '3888'], ['7', '6', '20', '1686'], ['5', '6', '19', '1317'],['13', '13', '5', '2853'], ['17', '2', '17', '3735']],
              [['18', '9', '6', '3564'], ['7', '6', '20', '1560'], ['5', '6', '19', '1227'],['13', '13', '5', '2619'], ['17', '2', '17', '3429']]]
        return X1

    if Number == 6:
        X1 = [[['18', '9', '6', '3600'], ['7', '6', '20', '1574'], ['5', '6', '19', '1237'], ['13', '13', '5', '2645'],['17', '2', '17', '3463']],
              [['18', '9', '6', '3654'], ['7', '6', '20', '1595'], ['5', '6', '19', '1252'], ['13', '13', '5', '2684'],['17', '2', '17', '3514']],
              [['18', '9', '6', '3888'], ['7', '6', '20', '1686'], ['5', '6', '19', '1317'], ['13', '13', '5', '2853'],['17', '2', '17', '3735']],
              [['18', '9', '6', '3942'], ['7', '6', '20', '1707'], ['5', '6', '19', '1332'], ['13', '13', '5', '2892'],['17', '2', '17', '3786']],
              [['18', '9', '6', '3708'], ['7', '6', '20', '1616'], ['5', '6', '19', '1267'], ['13', '13', '5', '2723'],['17', '2', '17', '3565']],
              [['18', '9', '6', '3726'], ['7', '6', '20', '1623'], ['5', '6', '19', '1272'], ['13', '13', '5', '2736'],['17', '2', '17', '3582']]]
        return X1

    if Number == 7:
        X1 = [[['2', '29', '12', '455'], ['29', '8', '1', '5666'], ['24', '1', '9', '4708'],['29', '23', '8', '5702'], [27, 10, 8,5299]],
              [['2', '29', '12', '449'], ['29', '8', '1', '5579'], ['24', '1', '9', '4636'],['29', '23', '8', '5615'], [27, 10, 8,5218]],
              [['2', '29', '12', '453'], ['29', '8', '1', '5637'], ['24', '1', '9', '4684'],['29', '23', '8', '5673'], [27, 10, 8,5272]],
              [['2', '29', '12', '449'], ['29', '8', '1', '5579'], ['24', '1', '9', '4636'],['29', '23', '8', '5615'], [27, 10, 8,5218]],
              [['2', '29', '12', '475'], ['29', '8', '1', '5956'], ['24', '1', '9', '4948'],['29', '23', '8', '5992'], [27, 10, 8,5569]],
              [['2', '29', '12', '505'], ['29', '8', '1', '6391'], ['24', '1', '9', '5308'],['29', '23', '8', '6427'], [27, 10, 8,5974]]]
        return X1




    if Number == 8:
        X1 = [[[5, 25, 20,1255], [30, 28, 17,6115], [23, 15, 17,4698],[30, 16, 5,5959], [28, 11, 19,5675]],
              [[5, 25, 20,1240], [30, 28, 17,6025], [23, 15, 17,4629],[30, 16, 5,5869], [28, 11, 19,5591]],
              [[5, 25, 20,1275], [30, 28, 17,6235], [23, 15, 17,4790],[30, 16, 5,6079], [28, 11, 19,5787]],
              [[5, 25, 20,1265], [30, 28, 17,6175], [23, 15, 17,4744],[30, 16, 5,6019], [28, 11, 19,5731]],
              [[5, 25, 20,1295], [30, 28, 17,6355], [23, 15, 17,4882],[30, 16, 5,6199], [28, 11, 19,5899]],
              [[5, 25, 20,1380], [30, 28, 17,6865], [23, 15, 17,5273],[30, 16, 5,6709], [28, 11, 19,6375]]]
        return X1



    if Number == 9:
        X1 = [[[6, 12, 11,1233], [9, 21, 17,1857], [21, 3, 1,4125],[27, 15, 18,5376], [17, 11, 11,3387]],
              [[6, 12, 11,1209], [9, 21, 17,1821], [21, 3, 1,4041],[27, 15, 18,5268], [17, 11, 11,3319]],
              [[6, 12, 11,1317], [9, 21, 17,1983], [21, 3, 1,4419],[27, 15, 18,5754], [17, 11, 11,3625]],
              [[6, 12, 11,1347], [9, 21, 17,2028], [21, 3, 1,4524],[27, 15, 18,5889], [17, 11, 11,3710]],
              [[6, 12, 11,1257], [9, 21, 17,1893], [21, 3, 1,4209],[27, 15, 18,5484], [17, 11, 11,3455]],
              [[6, 12, 11,1269], [9, 21, 17,1911], [21, 3, 1,4251],[27, 15, 18,5538], [17, 11, 11,3489]]]
        return X1


    if Number == 10:
        X1 = [[[19, 22, 24,4074], [23, 9, 6,4613], [18, 14, 30,3898],[21, 2, 9,4216], [8, 15, 27,1913]],
              [[19, 22, 24,4036], [23, 9, 6,4567], [18, 14, 30,3862],[21, 2, 9,4174], [8, 15, 27,1897]],
              [[19, 22, 24,4264], [23, 9, 6,4843], [18, 14, 30,4078],[21, 2, 9,4426], [8, 15, 27,1993]],
              [[19, 22, 24,4169], [23, 9, 6,4728], [18, 14, 30,3988],[21, 2, 9,4321], [8, 15, 27,1953]],
              [[19, 22, 24,4188], [23, 9, 6,4751], [18, 14, 30,4006],[21, 2, 9,4342], [8, 15, 27,1961]],
              [[19, 22, 24,3998], [23, 9, 6,4521], [18, 14, 30,3826],[21, 2, 9, 4132], [8, 15, 27,1881]]]
        return X1



    if Number == 11:
        X1 = [[[7, 23, 1,1502], [27, 8, 15,5479], [25, 10, 13,5079],[1, 21, 30,542], [16, 3, 28,3391]],
              [[7, 23, 1,1614], [27, 8, 15,5911], [25, 10, 13,5479],[1, 21, 30,558], [16, 3, 28,3647]],
              [[7, 23, 1,1523], [27, 8, 15,5560], [25, 10, 13,5154],[1, 21, 30,545], [16, 3, 28,3439]],
              [[7, 23, 1,1495], [27, 8, 15,5452], [25, 10, 13,5054],[1, 21, 30,541], [16, 3, 28,3375]],
              [[7, 23, 1,1558], [27, 8, 15,5695], [25, 10, 13,5279],[1, 21, 30,550], [16, 3, 28,3519]],
              [[7, 23, 1,1467], [27, 8, 15,5344], [25, 10, 13,4954],[1, 21, 30,537], [16, 3, 28,3311]]]
        return X1

    if Number == 12:
        X1 = [[['14', '12', '26', '2938'], ['16', '20', '25', '3342'], ['3', '16', '4', '647'],['11', '24', '16', '2311'], ['21', '28', '29', '4367']],
              [['14', '12', '26', '2924'], ['16', '20', '25', '3326'], ['3', '16', '4', '644'],['11', '24', '16', '2300'], ['21', '28', '29', '4346']],
              [['14', '12', '26', '2980'], ['16', '20', '25', '3390'], ['3', '16', '4', '656'],['11', '24', '16', '2344'], ['21', '28', '29', '4430']],
              [['14', '12', '26', '3050'], ['16', '20', '25', '3470'], ['3', '16', '4', '671'],['11', '24', '16', '2399'], ['21', '28', '29', '4535']],
              [['14', '12', '26', '3246'], ['16', '20', '25', '3694'], ['3', '16', '4', '713'],['11', '24', '16', '2553'], ['21', '28', '29', '4829']],
              [['14', '12', '26', '2994'], ['16', '20', '25', '3406'], ['3', '16', '4', '659'],['11', '24', '16', '2355'], ['21', '28', '29', '4451']]]
        return X1


    if Number == 13:
        X1 = [[[3, 15, 7,808], [21, 9, 3,4290], [29, 9, 8,5947],[5, 12, 1,1104], [16, 18, 16,3536]],
              [[3, 15, 7,787], [21, 9, 3,4143], [29, 9, 8,5744],[5, 12, 1,1069], [16, 18, 16,3424]],
              [[3, 15, 7,805], [21, 9, 3,4269], [29, 9, 8,5918],[5, 12, 1,1099], [16, 18, 16,3520]],
              [[3, 15, 7,802], [21, 9, 3,4248], [29, 9, 8,5889],[5, 12, 1,1094], [16, 18, 16,3504]],
              [[3, 15, 7,856], [21, 9, 3,4626], [29, 9, 8,6411],[5, 12, 1,1184], [16, 18, 16,3792]],
              [[3, 15, 7,871], [21, 9, 3,4731], [29, 9, 8,6556],[5, 12, 1,1209], [16, 18, 16,3872]]]
        return X1

    if Number == 14:
        X1 = [[[13, 4, 26, 2906], [8, 2, 11, 1731], [13, 6, 8, 2718],[21, 4, 17, 4407], [14, 11, 20, 3075]],
              [[13, 4, 26, 2893], [8, 2, 11, 1723], [13, 6, 8, 2705],[21, 4, 17, 4386], [14, 11, 20, 3061]],
              [[13, 4, 26, 3140], [8, 2, 11, 1875], [13, 6, 8, 2952],[21, 4, 17, 4785], [14, 11, 20, 3327]],
              [[13, 4, 26, 3205], [8, 2, 11, 1915], [13, 6, 8, 3017],[21, 4, 17, 4890], [14, 11, 20, 3397]],
              [[13, 4, 26, 3036], [8, 2, 11, 1811], [13, 6, 8, 2848],[21, 4, 17, 4617], [14, 11, 20, 3215]],
              [[13, 4, 26, 3166], [8, 2, 11, 1891], [13, 6, 8, 2978],[21, 4, 17, 4827], [14, 11, 20, 3355]]]
        return X1



    if Number == 15:
        X1 = [[[14, 9, 29,3210], [5, 19, 10,1253], [26, 21, 23,5652],[3, 26, 12,920], [11, 10, 17,2479]],
              [[14, 9, 29,3070], [5, 19, 10,1203], [26, 21, 23,5392],[3, 26, 12,890], [11, 10, 17,2369]],
              [[14, 9, 29,3224], [5, 19, 10,1258], [26, 21, 23,5678],[3, 26, 12,923], [11, 10, 17,2490]],
              [[14, 9, 29,3462], [5, 19, 10,1343], [26, 21, 23,6120],[3, 26, 12,974], [11, 10, 17,2677]],
              [[14, 9, 29,3210], [5, 19, 10,1253], [26, 21, 23,5652],[3, 26, 12,920], [11, 10, 17,2479]],
              [[14, 9, 29,3070], [5, 19, 10,1203], [26, 21, 23,5392],[3, 26, 12,890], [11, 10, 17,2369]]]
        return X1


    if Number == 16:
        X1 = [[[30, 8, 17,6252], [14, 4, 12,2952], [8, 15, 10,1801],[30, 10, 9,6202], [3, 23, 3,791]],
              [[30, 8, 17,5952], [14, 4, 12,2812], [8, 15, 10,1721],[30, 10, 9,5902], [3, 23, 3,761]],
              [[30, 8, 17,6342], [14, 4, 12,2994], [8, 15, 10,1825],[30, 10, 9,6292], [3, 23, 3,800]],
              [[30, 8, 17,5952], [14, 4, 12,2812], [8, 15, 10,1721],[30, 10, 9,5202], [3, 23, 3,761]],
              [[30, 8, 17,6012], [14, 4, 12,2840], [8, 15, 10,1737],[30, 10, 9,5962], [3, 23, 3,767]],
              [[30, 8, 17,5952], [14, 4, 12,2812], [8, 15, 10,1721],[30, 10, 9,5902], [3, 23, 3,761]]]
        return X1



    if Number == 17:
        X1 = [[[16, 7, 14,3402], [12, 10, 24,2692], [14, 30, 24,3178],[28, 6, 17,5861], [20, 4, 28,4328]],
              [[16, 7, 14,3226], [12, 10, 24,2560], [14, 30, 24,3024],[28, 6, 17,5553], [20, 4, 28,4108]],
              [[16, 7, 14,3434], [12, 10, 24,2716], [14, 30, 24,3206],[28, 6, 17,5917], [20, 4, 28,4368]],
              [[16, 7, 14,3290], [12, 10, 24,2608], [14, 30, 24,3080],[28, 6, 17,5665], [20, 4, 28,4188]],
              [[16, 7, 14,3658], [12, 10, 24,2884], [14, 30, 24,3402],[28, 6, 17,6309], [20, 4, 28,4648]],
              [[16, 7, 14,3610], [12, 10, 24,2848], [14, 30, 24,3360],[28, 6, 17,6225], [20, 4, 28,4588]]]
        return X1

    if Number == 18:
        X1 = [[[19, 3, 9,3911], [3, 23, 25,803], [16, 27, 26,3459],[11, 1, 4,2256], [11, 25, 6,2338]],
              [[19, 3, 9,3797], [3, 23, 25,785], [16, 27, 26,3363],[11, 1, 4,2190], [11, 25, 6,2272]],
              [[19, 3, 9,3778], [3, 23, 25,782], [16, 27, 26,3347],[11, 1, 4,2179], [11, 25, 6,2261]],
              [[19, 3, 9,3949], [3, 23, 25,809], [16, 27, 26,3491],[11, 1, 4,2278], [11, 25, 6,2360]],
              [[19, 3, 9,3854], [3, 23, 25,794], [16, 27, 26,3411],[11, 1, 4,2223], [11, 25, 6,2305]],
              [[19, 3, 9,3892], [3, 23, 25,800], [16, 27, 26,3443],[11, 1, 4,2245], [11, 25, 6,2327]]]
        return X1


    if Number == 19:
        X1 = [[[4, 21, 18,1062], [5, 23, 2,1130], [26, 30, 1,5433],[24, 20, 19,5147], [30, 14, 3,6203]],
              [[4, 21, 18,1014], [5, 23, 2,1070], [26, 30, 1,5121],[24, 20, 19,4859], [30, 14, 3,5843]],
              [[4, 21, 18,1054], [5, 23, 2,1120], [26, 30, 1,5381],[24, 20, 19,5099], [30, 14, 3,6143]],
              [[4, 21, 18,1046], [5, 23, 2,1110], [26, 30, 1,5329],[24, 20, 19,5051], [30, 14, 3,6083]],
              [[4, 21, 18,1138], [5, 23, 2,1225], [26, 30, 1,5927],[24, 20, 19,5603], [30, 14, 3,6773]],
              [[4, 21, 18,1038], [5, 23, 2,1100], [26, 30, 1,5277],[24, 20, 19,5003], [30, 14, 3,6023]]]
        return X1


    if Number == 20:
        X1 = [[[26, 30, 16,5828], [22, 24, 1,4742], [23, 1, 10,4842],[6, 6, 22,1592], [29, 5, 17,6204]],
              [[26, 30, 16,5516], [22, 24, 1,4478], [23, 1, 10,4566],[6, 6, 22,1520], [29, 5, 17,5856]],
              [[26, 30, 16,5932], [22, 24, 1,4830], [23, 1, 10,4934],[6, 6, 22,1616], [29, 5, 17,6320]],
              [[26, 30, 16,5776], [22, 24, 1,4698], [23, 1, 10,4796],[6, 6, 22,1580], [29, 5, 17,6146]],
              [[26, 30, 16,5724], [22, 24, 1,4654], [23, 1, 10,4750],[6, 6, 22,1568], [29, 5, 17,6088]],
              [[26, 30, 16,5750], [22, 24, 1,4676], [23, 1, 10,4773],[6, 6, 22,1574], [29, 5, 17,6117]]]
        return X1





def clear():
    root_powers_text.delete(0, 'end')
    root_powers_text_2.delete(1.0, 'end')
    Key_text.delete(0, 'end')

    enter_text_S1_No.config(state='normal')
    enter_text_S2_No.config(state='normal')
    enter_text_S3_No.config(state='normal')
    enter_text_S4_No.config(state='normal')
    enter_text_S5_No.config(state='normal')
    enter_text_S6_No.config(state='normal')

    enter_text_S1_Yes.config(state='normal')
    enter_text_S2_Yes.config(state='normal')
    enter_text_S3_Yes.config(state='normal')
    enter_text_S4_Yes.config(state='normal')
    enter_text_S5_Yes.config(state='normal')
    enter_text_S6_Yes.config(state='normal')





    enter_text_S1_No.delete(1.0, 'end')
    enter_text_S2_No.delete(1.0, 'end')
    enter_text_S3_No.delete(1.0, 'end')
    enter_text_S4_No.delete(1.0, 'end')
    enter_text_S5_No.delete(1.0, 'end')
    enter_text_S6_No.delete(1.0, 'end')

    enter_text_S1_Yes.delete(1.0, 'end')
    enter_text_S2_Yes.delete(1.0, 'end')
    enter_text_S3_Yes.delete(1.0, 'end')
    enter_text_S4_Yes.delete(1.0, 'end')
    enter_text_S5_Yes.delete(1.0, 'end')
    enter_text_S6_Yes.delete(1.0, 'end')

    enter_text_S1_No.config(state='disabled')
    enter_text_S2_No.config(state='disabled')
    enter_text_S3_No.config(state='disabled')
    enter_text_S4_No.config(state='disabled')
    enter_text_S5_No.config(state='disabled')
    enter_text_S6_No.config(state='disabled')

    enter_text_S1_Yes.config(state='disabled')
    enter_text_S2_Yes.config(state='disabled')
    enter_text_S3_Yes.config(state='disabled')
    enter_text_S4_Yes.config(state='disabled')
    enter_text_S5_Yes.config(state='disabled')
    enter_text_S6_Yes.config(state='disabled')




def gauss_elimination(A, B):
    n = len(A)
    for i in range(n):
        max_row = i
        for k in range(i + 1, n):
            if abs(A[k][i]) > abs(A[max_row][i]):
                max_row = k
        A[i], A[max_row] = A[max_row], A[i]
        B[i], B[max_row] = B[max_row], B[i]
        for k in range(i + 1, n):
            factor = A[k][i] / A[i][i]
            for j in range(i, n):
                A[k][j] -= factor * A[i][j]
            B[k] -= factor * B[i]
    x = [0] * n
    for i in range(n - 1, -1, -1):
        x[i] = B[i] / A[i][i]
        for k in range(i - 1, -1, -1):
            B[k] -= A[k][i] * x[i]
    return x

def MNK_metod(coefficients, y_values):
    solution = np.linalg.lstsq(coefficients, y_values,None)[0]
    return solution

def print_virash(X,K):
    sch = 0
    if K == 3:
        for i in X:
            if sch == 0:
                text = f"⎛{str(i[0])}x{sch+1} + {str(i[1])}x{sch+2} + {str(i[2])}x{sch+3} = {str(i[3])}"
                root_powers_text_2.insert('end', text)
                root_powers_text_2.insert('end', '\n')
            elif sch == 1:
                text = f"⎨{str(i[0])}x{sch} + {str(i[1])}x{sch+1} + {str(i[2])}x{sch+2} = {str(i[3])}"
                root_powers_text_2.insert('end', text)
                root_powers_text_2.insert('end', '\n')
            else:
                text = f"⎝{str(i[0])}x{sch-1} + {str(i[1])}x{sch} + {str(i[2])}x{sch+1} = {str(i[3])}"
                root_powers_text_2.insert('end', text)
                root_powers_text_2.insert('end', '\n')
            sch += 1
    else:
        for i in X:
            if sch == 0:
                text = f"⎛{str(i[0])}x{sch+1} + {str(i[1])}x{sch+2} + {str(i[2])}x{sch+3} = {str(i[3])}"
                root_powers_text_2.insert('end', text)
                root_powers_text_2.insert('end', '\n')
            elif sch == 1:
                text = f"⎜{str(i[0])}x{sch} + {str(i[1])}x{sch+1} + {str(i[2])}x{sch+2} = {str(i[3])}"
                root_powers_text_2.insert('end', text)
                root_powers_text_2.insert('end', '\n')

            elif sch == 2:
                text = f"⎨{str(i[0])}x{sch-1} + {str(i[1])}x{sch} + {str(i[2])}x{sch+1} = {str(i[3])}"
                root_powers_text_2.insert('end', text)
                root_powers_text_2.insert('end', '\n')

            elif sch == 3:
                text = f"⎜{str(i[0])}x{sch-2} + {str(i[1])}x{sch-1} + {str(i[2])}x{sch} = {str(i[3])}"
                root_powers_text_2.insert('end', text)
                root_powers_text_2.insert('end', '\n')

            else:
                text = f"⎝{str(i[0])}x{sch-3} + {str(i[1])}x{sch-2} + {str(i[2])}x{sch-1} = {str(i[3])}"
                root_powers_text_2.insert('end', text)
                root_powers_text_2.insert('end', '\n')
            sch += 1




    root_powers_text_2.insert('end',"\n")
    return

def podshet(X, K):
    New_X = [list(map(int, x)) for x in X]
    V4 = []
    for i in range(K):
        V4.append(New_X[i])
        #R = random.choice(New_X)
        #New_X.remove(R)
        #V4.append(R)

    print_virash(V4,K)

    b = []
    for i in range(len(V4)):
        b.append(V4[i][-1])
        V4[i].remove(V4[i][-1])

    #print(V4)
    if K == 3:
        print(V4)
        print(b)
        resutl = gauss_elimination(V4, b)
        print(resutl)
        return resutl[0]
    elif K == 5:
        resutl = MNK_metod(V4, b)
        return resutl[0]


def main():
    if root_powers_text.get().isdigit() and isinstance(int(root_powers_text.get()), int) :
        if (int(root_powers_text.get()) > 0) and (int(root_powers_text.get()) < 21):
            Var = int(root_powers_text.get())
        else:
            showwarning(title="Предупреждение", message=f"Такого варианта нет! {root_powers_text.get()} ∉ (1..20)")
            return

    else:
        showwarning(title="Предупреждение", message="Это не число\целое число")
        return

    if Key_text.get().isdigit() and isinstance(int(Key_text.get()), int):
        if (int(Key_text.get()) == 3) or (int(Key_text.get()) == 5):
            K = int(Key_text.get())
        else:
            showwarning(title="Предупреждение", message=f"Такого варианта нет!\n {Key_text.get()} != 3|5")
            return
    else:
        showwarning(title="Предупреждение", message="Это не число\целое число")
        return

    Var = Variant(Var)
    Mass_otv = []
    for i in range(6):
        Mass_otv.append(podshet(Var[i], K))

    for i in range(len(Mass_otv)):
        Mass_otv[i] = round(Mass_otv[i])

    enter_text_S1_No.config(state='normal')
    enter_text_S1_No.insert('1.0',str(Mass_otv[0]))
    enter_text_S1_No.config(state='disabled')

    enter_text_S2_No.config(state='normal')
    enter_text_S2_No.insert('1.0',str(Mass_otv[1]))
    enter_text_S2_No.config(state='disabled')

    enter_text_S3_No.config(state='normal')
    enter_text_S3_No.insert('1.0',str(Mass_otv[2]))
    enter_text_S3_No.config(state='disabled')

    enter_text_S4_No.config(state='normal')
    enter_text_S4_No.insert('1.0',str(Mass_otv[3]))
    enter_text_S4_No.config(state='disabled')

    enter_text_S5_No.config(state='normal')
    enter_text_S5_No.insert('1.0',str(Mass_otv[4]))
    enter_text_S5_No.config(state='disabled')

    enter_text_S6_No.config(state='normal')
    enter_text_S6_No.insert('1.0',str(Mass_otv[5]))
    enter_text_S6_No.config(state='disabled')



    secret = [bytes([num]).decode('cp1251', errors='replace') for num in Mass_otv]
    enter_text_S1_Yes.config(state='normal')
    enter_text_S1_Yes.insert('1.0', str(secret[0]))
    enter_text_S1_Yes.config(state='disabled')

    enter_text_S2_Yes.config(state='normal')
    enter_text_S2_Yes.insert('1.0', str(secret[1]))
    enter_text_S3_Yes.config(state='disabled')

    enter_text_S3_Yes.config(state='normal')
    enter_text_S3_Yes.insert('1.0', str(secret[2]))
    enter_text_S3_Yes.config(state='disabled')

    enter_text_S4_Yes.config(state='normal')
    enter_text_S4_Yes.insert('1.0', str(secret[3]))
    enter_text_S4_Yes.config(state='disabled')

    enter_text_S5_Yes.config(state='normal')
    enter_text_S5_Yes.insert('1.0', str(secret[4]))
    enter_text_S5_Yes.config(state='disabled')

    enter_text_S6_Yes.config(state='normal')
    enter_text_S6_Yes.insert('1.0', str(secret[5]))
    enter_text_S6_Yes.config(state='disabled')
    print(secret)
    return













root2 = tk.Tk()
root2.title("Black")
root2.geometry("350x500")


root_powers_text = tk.Entry()
root_powers_text.place(x=10,y=30, width=35)

root_powers_text_2 = tk.Text()
root_powers_text_2.place(x=10,y=110, width=300,height=100)

Key_text = tk.Entry()
Key_text.place(x=145,y=30, width=80)

enter_text = tk.Label(root2, text="Enter variant:", font=("Matura MT Script Capitals", 12))
enter_text.place(x=10,y=1)

enter_text_2 = tk.Label(root2, text="Equation:", font=("Matura MT Script Capitals", 12))
enter_text_2.place(x=10,y=80)

enter_text_X1 = tk.Label(root2, text="S1:", font=("Matura MT Script Capitals", 12))
enter_text_X1.place(x=10,y=250)

enter_text_X2 = tk.Label(root2, text="S2:", font=("Matura MT Script Capitals", 12))
enter_text_X2.place(x=45,y=250)

enter_text_X3 = tk.Label(root2, text="S3:", font=("Matura MT Script Capitals", 12))
enter_text_X3.place(x=90,y=250)

enter_text_X4 = tk.Label(root2, text="S4:", font=("Matura MT Script Capitals", 12))
enter_text_X4.place(x=145,y=250)

enter_text_X5 = tk.Label(root2, text="S5:", font=("Matura MT Script Capitals", 12))
enter_text_X5.place(x=185,y=250)

enter_text_X6 = tk.Label(root2, text="S6:", font=("Matura MT Script Capitals", 12))
enter_text_X6.place(x=225,y=250)

enter_text_S1_No = tk.Text()
enter_text_S1_No.place(x=10,y=280, width=30,height=20)
enter_text_S1_No.config(state='disabled')

enter_text_S1_Yes = tk.Text(font=("Helvetica", 10))
enter_text_S1_Yes.place(x=10,y=310, width=30,height=20)
enter_text_S1_Yes.config(state='disabled')

enter_text_S2_No = tk.Text()
enter_text_S2_No.place(x=45,y=280, width=30,height=20)
enter_text_S2_No.config(state='disabled')

enter_text_S2_Yes = tk.Text(font=("Helvetica", 10))
enter_text_S2_Yes.place(x=45,y=310, width=30,height=20)
enter_text_S2_Yes.config(state='disabled')

enter_text_S3_No = tk.Text()
enter_text_S3_No.place(x=90,y=280, width=30,height=20)
enter_text_S3_No.config(state='disabled')

enter_text_S3_Yes = tk.Text(font=("Helvetica", 10))
enter_text_S3_Yes.place(x=90,y=310, width=30,height=20)
enter_text_S3_Yes.config(state='disabled')

enter_text_S4_No = tk.Text()
enter_text_S4_No.place(x=145,y=280, width=30,height=20)
enter_text_S4_No.config(state='disabled')

enter_text_S4_Yes = tk.Text(font=("Helvetica", 10))
enter_text_S4_Yes.place(x=145,y=310, width=30,height=20)
enter_text_S4_Yes.config(state='disabled')

enter_text_S5_No = tk.Text()
enter_text_S5_No.place(x=185,y=280, width=30,height=20)
enter_text_S5_No.config(state='disabled')

enter_text_S5_Yes = tk.Text(font=("Helvetica", 10))
enter_text_S5_Yes.place(x=185,y=310, width=30,height=20)
enter_text_S5_Yes.config(state='disabled')

enter_text_S6_No = tk.Text()
enter_text_S6_No.place(x=225,y=280, width=30,height=20)
enter_text_S6_No.config(state='disabled')

enter_text_S6_Yes = tk.Text(font=("Helvetica", 10))
enter_text_S6_Yes.place(x=225,y=310, width=30,height=20)
enter_text_S6_Yes.config(state='disabled')


label_key = tk.Label(root2, text="Enter K:", font=("Matura MT Script Capitals", 12))
label_key.place(x=145,y=1)


code = tk.Button(root2, text="Посчитать", command=main, font=("Helvetica", 12), bg="#CD950C", fg="black")
code.place(x=120,y=400)


Clear_btn = tk.Button(root2, text="Очистить",command=clear, font=("Helvetica", 12), bg="#CD950C", fg="black")
Clear_btn.place(x=125,y=450)




root2.mainloop()