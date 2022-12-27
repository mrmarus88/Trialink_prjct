import pandas as pd 
import numpy as np
import pretty_html_table
import views

#import csv template
terminals = pd.read_csv('D:\\python\\UpdateDB\\template_for_web.csv')
terminals_calc = pd.DataFrame(terminals)
#fill the dataframe by "0"
terminals_calc = terminals_calc.fillna(0)

version_1_base = pd.DataFrame({'Position':['EPC 1',
                                 'EPC 2',
                                 'licence 150 1',
                                 'licence 150 2',
                                 'iHSS 150',
                                 'iPCRF 150',
                                 'NMS 15endb',
                                 'NMS HW',
                                 'MARS_MTM'],
                    'Quantity': [1,1,1,1,1,2,1,1,1],
                    'Cost': [3000,
                               3000,
                               0,
                               0,
                               675,
                               580,
                               4000,
                               1000,
                               0],
                    'Price': [24000,
                                   24000,
                                   0,
                                   0,
                                   5400,
                                   4640,
                                   16000,
                                   3360,
                                   3840],
                    'Total price': [24000,
                                   24000,
                                   0,
                                   0,
                                   5400,
                                   9280,
                                   16000,
                                   3360,
                                   3840]}) 

version_2_base = pd.DataFrame({'Position':['EPC 1',
                                 'EPC 2',
                                 'licence 1000 1',
                                 'licence 1000 2',
                                 'iHSS 500',
                                 'iPCRF 500',
                                 'NMS 15endb',
                                 'NMS HW',
                                 'MARS_MTM'],
                     'Quantity': [1,1,1,1,2,4,1,1,1],
                     'Cost': [9800,
                               4900,
                               0,
                               0,
                               2250,
                               975,
                               4000,
                               1000,
                               0],
                     'Price': [78400,
                                   39200,
                                   0,
                                   0,
                                   18000,
                                   7800,
                                   16000,
                                   3360,
                                   3840],
                     'Total price': [78400,
                                   39200,
                                   0,
                                   0,
                                   36000,
                                   31200,
                                   3360,
                                   16000,
                                   3840]}) 

#additional licences
additional = pd.DataFrame({'Position':['EPC 50',
                                 'iHSS 50',
                                 'iPCRF 50',
                                 'iHSS 150',
                                 'iPCRF 150',
                                 'iHSS 500',
                                 'iPCRF 500',
                                 'non-Telad eNodeB',
                                 'NMS add endB',
                                 'SFP+10G',
                                 'L2 service',
                                 'MARS NMS SW 5endB',
                                 'MARS NMS SW 1endB',
                                 'RONET SGW',
                                 'RONET RGW',
                                 'ESR 21 Router',
                                 'RONET Compact pro 300',
                                 'RONET Compact pro 500',
                                 '42U',
                                 'SCAT UPS 3000',
                                 '7U box',
                                 'MARS UPS HS-48'],
                           
                     'Quantity': [2,1,2,1,2,1,2,2,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
                     
                        'Cost': [400, #EPC 50
                                225, #iHSS 50
                                97.5,#iPCRF 50
                                675, #iHSS 150
                                580, #iPCRF 150
                                2250,#iHSS 500
                                975, #iPCRF 500
                                1500,#non-Telad eNodeB
                                400, #NMS add endB
                                0,    #SFP+10G
                                0,   #L2 service
                                0,   #MARS NMS SW 5endB
                                0,    #MARS NMS SW 1endB
                                0,   #RONET SGW
                                0,   #RONET RGW
                                0,   #ESR 21 Router
                                0,  #RONET Compact pro 300
                                0,  #RONET Compact pro 500
                                0,   #42U
                                0,   #SCAT UPS 3000
                                0,   #7U box
                                0],  #MARS UPS HS-48
                        
                     'Price': [ 3200,   #EPC 50
                                    1800,   #iHSS 50     
                                    780,    #iPCRF 50
                                    5400,   #iHSS 150
                                    4640,   #iPCRF 150
                                    18000,  #iHSS 500
                                    7800,   #iPCRF 500
                                    12000,  #non-Telad eNodeB
                                    1600,   #NMS add endB
                                    125,    #SFP+10G
                                    3500,   #L2 service
                                    2500,   #MARS NMS SW 5endB
                                    200,    #MARS NMS SW 1endB
                                    9000,   #RONET SGW
                                    5400,   #RONET RGW
                                    5760,   #ESR 21 Router
                                    12000,  #RONET Compact pro 300
                                    14000,  #RONET Compact pro 500
                                    1800,   #42U
                                    2820,   #SCAT UPS 3000
                                    1100,   #7U box
                                    460],}) #MARS UPS HS-48

Position = ['EPC 50',
            'iHSS 50',
            'iPCRF 50',
            'iHSS 150',
            'iPCRF 150',
            'iHSS 500',
            'iPCRF 500',
            'non-Telad eNodeB licence',
            'NMS add endB',
            'SFP+10G',
            'L2 service',
            'MARS NMS SW 5endB',
            'MARS NMS SW 1endB',
            'RONET SGW',
            'RONET RGW',
            'ESR 21 Router',
            'RONET Compact pro 300',
            'RONET Compact pro 500',
            '42U',
            'SCAT UPS 3000',
            '7U box',
            'MARS UPS HS-48']
additional = additional.fillna(0)

#input and chose packet version
print ("Input Packet version: ")
Version = int(input())
version_1 = version_1_base[['Position','Quantity','Price','Total price']]
version_2 = version_2_base[['Position','Quantity','Price','Total price']]

if Version == 1:
    vers = version_1
elif Version == 2:
    vers = version_2
else:
    vers = 'Need to check packet version'

#input subs
print ("Input Subscribers count: ")
subs = int(input())

#input additional positions
print ("Additional positions: ", "eNodeB all", sep = '\n')
add_enodeb = int(input())       # add count of all eNodeB on prjct 
print ("non Telrad eNodeB: ")
add_nontelrad = int(input())    # add non-Telrad enodeB count
print ("42U: ")
add_42u = int(input())          # add 42U box count
print ("7U box: ")
add_7ubox = int(input())        # add 7U box count
print ("Router: ")
add_Router = int(input())       # add Router count
print ("SGW: ")
add_SGW = int(input())          # add SGW count
print ("RGW: ")
add_RGW = int(input())          # add RGW count
print ("L2 service: ")
add_l2 = int(input())           # add L2 service count
print ("SFP 10G+: ")
add_sfp10 = int(input())        # add SFP 10G+ count


#Count of EPC , iHSS, iPCRF if subs < 650 : 
count_epc = ()
if np.array(int(((subs-150)/50)*2)) < 1:  # EPC
    count_epc = 2
else: 
    count_epc  = np.array(int(((subs-150)/50)*2))
    
count_hss = ()                           # sub<650   iHSS
if np.array(int(((subs-150)/50))) < 1:  
    count_hss = 1
else: 
    count_hss = np.array(int(((subs-150)/50)))
    
count_pcrf =  ()                         # sub<650   iPCRF
if np.array(int(((subs-150)/50)*2)) < 1:  
    count_pcrf = 2
else: 
    count_pcrf = np.array(int(((subs-150)/50)*2))
    

#Count iHSS, iPCRF if 1000 > subs > 650 : 
count_hss_2 = np.array(int(((subs-650)/50)))    # sub>650   iHSS
count_pcrf_2 = np.array(int(((subs-650)/50)*2)) # sub>650   iPCRF


#Count EPC, iHSS, iPCRF if subs > 1000 : 
count_epc_2_2 =  ()
if np.array(int(((subs-1000)/50)*2)) < 1:      # EPC > 1000
    count_epc_2_2 = 2
else: 
    count_epc_2_2  = np.array(int(((subs-1000)/50)*2))
    
count_hss_2_2 = ()                            # sub>1000   iHSS 500
if np.array(int(((subs-1000)/50))) < 1:  
    count_hss_2_2 = 1
else: 
    count_hss_2_2 = np.array(int(((subs-1000)/50)))

count_pcrf_2_2 =  ()
if np.array(int(((subs-1000)/50)*2)) < 1:      # sub>1000   iPCRF 500
    count_pcrf_2_2 = 2
else: 
    count_pcrf_2_2  = np.array(int(((subs-1000)/50)*2))


#Total price (price*count) for EPC, iHSS, iPCRF positions:
Total_price_epc = int((((subs-150)/50)*2)*additional['Price'][0])    # sub<650   EPC
Total_price_HSS = int(((subs-150)/50)*additional['Price'][1])        # sub<650   iHSS
Total_price_PCRF = int((((subs-150)/50)*2)*additional['Price'][2])   # sub<650   iPCRF



#additionals licences and HW:
less_150 = pd.DataFrame([
                {'Position': "Additional licences not need",'Quantity': '','Price': '', 'Total price': 0}
                ])

subs_1000 = pd.DataFrame([
                {'Position': "Additional licences not need",'Quantity': '','Price': '', 'Total price': 0}
                ])

less_650 = pd.DataFrame([
                {'Position': Position[0],'Quantity': count_epc,'Price': additional['Price'][0], 'Total price': Total_price_epc},
                {'Position': Position[1],'Quantity': count_hss,'Price': additional['Price'][1], 'Total price': Total_price_HSS},
                {'Position': Position[2],'Quantity': count_pcrf,'Price': additional['Price'][2], 'Total price': Total_price_PCRF}
                ])

subs_650 = pd.DataFrame([
                {'Position': Position[0],'Quantity': count_epc,'Price': additional['Price'][0], 'Total price': Total_price_epc},
                {'Position': Position[5],'Quantity': 1,'Price': additional['Price'][5], 'Total price': additional['Price'][5]},
                {'Position': Position[6],'Quantity': 2,'Price': additional['Price'][6], 'Total price': (additional['Price'][6]*2)}
                ])

subs_650_1000 = pd.DataFrame([
                {'Position': Position[0],'Quantity': count_epc,'Price': additional['Price'][0], 'Total price': Total_price_epc},
                {'Position': Position[5],'Quantity': 1,'Price': additional['Price'][5], 'Total price': additional['Price'][5]},
                {'Position': Position[1],'Quantity': count_hss_2,'Price': additional['Price'][1], 'Total price': Total_price_HSS},
                {'Position': Position[6],'Quantity': 2,'Price': additional['Price'][6], 'Total price': (additional['Price'][6]*2)},
                {'Position': Position[2],'Quantity': count_pcrf_2,'Price': additional['Price'][2], 'Total price': Total_price_PCRF}
                ])

subs_1000_1500 = pd.DataFrame([
                {'Position': Position[0],'Quantity': count_epc_2_2, 'Price': additional['Price'][0], 'Total price': Total_price_epc},
                {'Position': Position[1],'Quantity': count_hss_2_2, 'Price': additional['Price'][1], 'Total price': Total_price_HSS},
                {'Position': Position[2],'Quantity': count_pcrf_2_2,'Price': additional['Price'][2], 'Total price': Total_price_PCRF}
                ])

subs_1500 = pd.DataFrame([
                {'Position': Position[0],'Quantity': count_epc_2_2, 'Price': additional['Price'][0], 'Total price': Total_price_epc},
                {'Position': Position[5],'Quantity': 1, 'Price': additional['Price'][5], 'Total price': additional['Price'][5]},
                {'Position': Position[6],'Quantity': 2,'Price': additional['Price'][6], 'Total price': (additional['Price'][6]*2)}  
                ])

print('Packet version: #' ,Version, '\n', vers)

if  subs <= 150:
            print('Additional Core licences: ', "Additional licences not need", sep = '\n')
            addi = less_150
elif subs < 650:
            print('Additional Core licences: ', less_650, sep = '\n')
            addi = less_650
elif subs == 650:
            print('Additional Core licences: ', subs_650, sep = '\n')
            addi = subs_650
elif subs > 650:
            if subs < 1000:
                    print('Additional Core licences: ', subs_650_1000, sep = '\n')
                    addi = subs_650_1000
            elif subs >= 1000:
                    if subs == 1000:
                            print('Additional Core licences: ', "Additional licences not need", sep = '\n')
                            addi = subs_1000
                    elif subs > 1000: 
                            print('Additional Core licences: ', subs_1000_1500, sep = '\n')      
                            addi = subs_1000_1500
                    elif subs == 1500:
                            print('Additional Core licences: ', subs_1500, sep = '\n')  
                            addi = subs_1500
else:
            print('Need to check versions')
            addi = 'Need to check versions'

#Additionals HW+SW equipment:
#Poc server count
server_POC = ()  
if  subs <= 300:
        server_POC = "RONET Compact pro 300"
        price_poc = additional['Price'][16]
        count_poc = 1
        totalprice_poc = count_poc*price_poc
elif subs <=500:
        server_POC = "RONET Compact pro 500"
        price_poc = additional['Price'][17]
        count_poc = 1
        totalprice_poc = price_poc*count_poc
else: 
    server_POC = "RONET Profeccional 10 000"
    price_poc = "-"
    count_poc = "-"
    totalprice_poc = 0
    
#NMS Telrad additional licences:
telrad_count = add_enodeb-add_nontelrad
add_telrad_nms_count = ()
if telrad_count <= 15:
    add_telrad_nms_count = 0
    price_telrad_nms = "-"
    total_price_add_telrad_nms = 0
else:
    add_telrad_nms_count = telrad_count - 15
    price_telrad_nms = additional['Price'][8]
    total_price_add_telrad_nms = price_telrad_nms*add_telrad_nms_count

#non-Telrad additional licences + Mars NMS lic:
if add_nontelrad > 0:
    nontelrad_lic = add_nontelrad*2
    nontelrad_price = additional['Price'][7]
    totalprice_nontelrad = nontelrad_price*nontelrad_lic
    if nontelrad_lic <= 5:
        mars_nms_lic_5 = 1
        mars_nms_lic_1 = 0
        price_mars_nms_lic_5 = additional['Price'][11]
        price_mars_nms_lic_1 = 0
        totalprice_mars_nms_lic_5 = price_mars_nms_lic_5
        totalprice_mars_nms_lic_1 = 0
    else:
        mars_nms_lic_5 = 1
        mars_nms_lic_1 =  add_nontelrad - 5
        price_mars_nms_lic_5 = additional['Price'][11]
        price_mars_nms_lic_1 = additional['Price'][12]
        totalprice_mars_nms_lic_5 = price_mars_nms_lic_5
        totalprice_mars_nms_lic_1 = price_mars_nms_lic_1*mars_nms_lic_1
else:
    nontelrad_lic = "-"
    nontelrad_price = "-"
    totalprice_nontelrad = 0
    mars_nms_lic_5 = "-"
    price_mars_nms_lic_5 = "-"
    totalprice_mars_nms_lic_5 = 0
    mars_nms_lic_1 = "-"
    price_mars_nms_lic_1 = "-"
    totalprice_mars_nms_lic_1 = 0



#42U + 7U box + UPS:

if add_42u > 0:
    count_42 = add_42u
    price_42 = additional['Price'][18]
    totalprice_42 = count_42*price_42
    count_skat = count_42
    price_skat = additional['Price'][19]
    totalprice_skat = count_skat*price_skat
else: 
    additional['Position'][18] = "-"
    count_42 = "-"
    price_42 = "-"
    totalprice_42 = 0
    additional['Position'][19] = "-"
    count_skat = "-"
    price_skat = "-"
    totalprice_skat = 0
    
if add_7ubox > 0 :
    count_7 = add_7ubox
    price_7 = additional['Price'][20]
    totalprice_7 = count_7*price_7
    count_mars_ups = count_7
    price_mars_ups = additional['Price'][21]
    totalprice_mars_ups = count_mars_ups*price_mars_ups
else:
    count_7 = "-"
    price_7 = "-"
    totalprice_7 = 0
    count_mars_ups = "-"
    price_mars_ups = "-"
    totalprice_mars_ups = 0

#Router, SGW, RGW, SFP10G, L2_service:
if add_Router <= 0:     # add Router count
    count_router = "-"
    price_router = "-"
    totralprice_router = 0
else:
    count_router = add_Router
    price_router = additional['Price'][15]
    totralprice_router = count_router*price_router
    
if add_SGW <= 0:   # add SGW count
    count_SGW = "-"
    price_SGW= "-"
    totralprice_SGW = 0
else:
    count_SGW = add_SGW
    price_SGW = additional['Price'][13]
    totralprice_SGW = count_SGW*price_SGW
    
if add_RGW <= 0:  # add RGW count
    count_RGW = "-"
    price_RGW = "-"
    totalprice_RGW = 0
else:
    count_RGW = add_RGW
    price_RGW = additional['Price'][14]
    totalprice_RGW = count_RGW*price_RGW
    
if add_l2 <= 0:     # add L2 service count
    count_l2 = "-"
    price_l2 = "-"
    totalprice_l2 = 0   
else:
    count_l2 = add_l2
    price_l2 = additional['Price'][10]
    totalprice_l2 = count_l2*price_l2
    
if add_sfp10 <= 0:    # add SFP 10G+ count
    count_sfp = "-"
    price_sfp = "-"
    totalprice_sfp = 0
else:
    count_sfp = add_sfp10
    price_sfp = additional['Price'][9]
    totalprice_sfp = count_sfp*price_sfp
        
hw_sw =  pd.DataFrame([
    {'Position': server_POC, 'Quantity': count_poc, 'Price': price_poc, 'Total price': totalprice_poc},
    {'Position': Position[8], 'Quantity': add_telrad_nms_count, 'Price': price_telrad_nms, 'Total price': total_price_add_telrad_nms},
    {'Position': Position[7], 'Quantity': nontelrad_lic,'Price': nontelrad_price, 'Total price': totalprice_nontelrad},
    {'Position': Position[11], 'Quantity': mars_nms_lic_5, 'Price': price_mars_nms_lic_5, 'Total price': totalprice_mars_nms_lic_5},
    {'Position': Position[12], 'Quantity': mars_nms_lic_1 , 'Price': price_mars_nms_lic_1 , 'Total price': totalprice_mars_nms_lic_1 },
    {'Position': Position[18], 'Quantity': count_42, 'Price': price_42, 'Total price': totalprice_42},
    {'Position': Position[19], 'Quantity': count_skat, 'Price': price_skat, 'Total price': totalprice_skat},
    {'Position': Position[20], 'Quantity': count_7, 'Price': price_7 , 'Total price': totalprice_7},
    {'Position': Position[21], 'Quantity': count_mars_ups, 'Price': price_mars_ups, 'Total price': totalprice_mars_ups},
    {'Position': Position[15], 'Quantity': count_router, 'Price': price_router, 'Total price': totralprice_router},
    {'Position': Position[13], 'Quantity': count_SGW, 'Price': price_SGW, 'Total price': totralprice_SGW},
    {'Position': Position[14], 'Quantity': count_RGW, 'Price': price_RGW, 'Total price': totalprice_RGW},
    {'Position': Position[10], 'Quantity': count_l2, 'Price': price_l2 , 'Total price': totalprice_l2},
    {'Position': Position[9], 'Quantity': count_sfp, 'Price': price_sfp , 'Total price': totalprice_sfp}
    ])        

print(
                'Additional HW+SW equipment: ', '\n',
                'eNodeB all: ', add_enodeb, '\n',
                'eNodeB Telrad: ', add_enodeb-add_nontelrad,'\n',
                'eNodeB non-Telrad: ', add_nontelrad,'\n',
                hw_sw)


#summary.style.applymap('font-weight: bold',
#                  subset=pd.IndexSlice[summary.index[summary.index=='Total'], :])
        
#Null index's in DataFrame - for beauty view.
title_1 = pd.DataFrame([
    {'Position': 'Core Packet: #', 'Quantity': Version, 'Price': '', 'Total price': 0},
    {'Position': '', 'Quantity': '', 'Price': '', 'Total price': 0}])
title_1.style.apply('font-weight: bold')

title_2 = pd.DataFrame([
    {'Position': '', 'Quantity': '', 'Price': 'Totally for Core packet:', 'Total price': vers['Total price'].sum()},
    {'Position': '', 'Quantity': '', 'Price': '', 'Total price': 0},
    {'Position': ('Additional Core licences: '), 'Quantity': '', 'Price': '', 'Total price': 0}]) 

title_3 = pd.DataFrame([
    {'Position': '', 'Quantity': '', 'Price': 'Totally for Additional licences:', 'Total price': addi['Total price'].sum()},
    {'Position': '', 'Quantity': '', 'Price': '', 'Total price': 0},
    {'Position': ('Additional HW+SW equipment: '), 'Quantity': '', 'Price': '', 'Total price': 0}]) 
total_hw_sw = pd.DataFrame([
    {'Position': '', 'Quantity': '', 'Price': 'Totally for additional HW and SW:', 'Total price': hw_sw['Total price'].sum()}]) 

#Make tables with titels
KP_total = pd.concat([title_1,vers,title_2,addi,title_3,hw_sw,total_hw_sw],sort= False, axis=0)
KP_calc  = pd.concat([vers,addi,hw_sw],sort= False, axis=0)
#KP_calc = KP_calc.fillna(0)

#Calculate Total price for all quantity in column:
total = pd.DataFrame([
    {'Position': '', 'Quantity': '', 'Price': '', 'Total price': ''},
    {'Position': '', 'Quantity': '', 'Price': '', 'Total price': ''},
    {'Position': '', 'Quantity': '', 'Price': 'Project total price: ', 'Total price': KP_calc['Total price'].sum()}]) 

#Make table Total + Main
KP_calc_final = pd.concat([KP_total,total],sort= False, axis=0)


#transform DataFrame in Table 
html_KP_calc = pretty_html_table.build_table(KP_calc_final
                                                ,'blue_light'
                                                , font_size='medium'
                                                , text_align='left'
                                                , width='auto'
                                                , index=False)

html_write = (html_KP_calc, '\n' , total)

#write html to file 
text_file = open("main/templates/show_result_calc.html", "w") 
text_file.write(html_KP_calc)
#text_file.write(''.join(str(total)))

print(views.export())