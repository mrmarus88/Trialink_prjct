from openpyxl import Workbook
import pandas as pd 
import numpy as np
import pretty_html_table
import math


def calc():
    #import csv template
    export_values = pd.DataFrame(pd.read_csv('Trialink\\test_export.csv')).fillna(0)

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
                                    'MARS UPS HS-48',
                                    'RPV-20000-100 (SW +300 subs)',
                                    'Ronet Professional HW',
                                    'Ronet Professional add licences (+100 subs)'],
                            
                        'Quantity': [2,1,2,1,2,1,2,2,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
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
                                        460,    #MARS UPS HS-48
                                        40000,  #RPV-20000-100 (SW +300 subs)
                                        4000,   #Ronet Professional HW
                                        1000]}).fillna(0) #Ronet Professional add licences (+100 subs)

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
                'MARS UPS HS-48',
                'MARS UPS HS-48,RPV-20000-100 (SW +300 subs)',
                'Ronet Professional HW',
                'Ronet Professional add licences (+100 subs)']
    
    bts_position = pd.DataFrame({'Position':['eB01H03112',  #0
                                            'eB01M04112',   #1
                                            'eB01M05112',   #2
                                            'eB01L06112',   #3
                                            'eB01L37112',   #4d
                                            'eB03H08112',   #5
                                            'eB03H10112',   #6
                                            'eB03M11112',   #7
                                            'eB03M12112',   #8
                                            'eB03L13112',   #9
                                            'eB03L38112',   #10
                                            'eB05H15112',   #11
                                            'eB05H17112',   #12
                                            'eB05M18112',   #13
                                            'eB05M19112',   #14
                                            'eB08H20112',   #15
                                            'eB08H22112',   #16
                                            'eB08M23112',   #17
                                            'eB08M24112',   #18
                                            'eB28H25112',   #19
                                            'eB31M26112',   #20
                                            'eB33L45012',   #21
                                            'eB33H47012',   #22
                                            'eB38L27012',   #23
                                            'eB39L46012',   #24
                                            'eB39H48012',   #25
                                            'eB40H28014',   #26
                                            'eB40L29012',   #27
                                            'eB41H30014',   #28
                                            'eB41L31012',   #29
                                            'eB42L32012',   #30
                                            'eB43L33012',   #31
                                            'eB42H39014',   #32
                                            'eB43H40014',   #33
                                            'eB42M41014',   #34
                                            'eB43M42014',   #35
                                            'eB48M43014',   #36
                                            'eB46L44014',   #37
                                            'eB48L34012',   #38
                                            'eB87M35112',   #39
                                            'eB88M36112',   #40
                                            'eB01H02122',   #41     distrib
                                            'eB01L07122',   #42     distrib
                                            'eB03H09122',   #43     distrib
                                            'eB03L14122',   #44     distrib
                                            'eB05H16122',   #45     distrib
                                            'eB08H21122'],  #46
                                 'Price': [5530,#0
                                        1850,   #1
                                        2930,   #2
                                        0,      #3
                                        0,      #4
                                        0,      #5
                                        5530,   #6
                                        1850,   #7
                                        2930,   #8
                                        0,      #9
                                        0,      #10
                                        0,      #11
                                        5530,   #12
                                        1850,   #13
                                        2930,   #14
                                        0,      #15
                                        5530,   #16
                                        1850,   #17
                                        2930,   #18
                                        0,      #19
                                        0,      #20
                                        0,      #21
                                        0,      #22
                                        0,      #23
                                        0,      #24
                                        0,      #25
                                        21980,  #26
                                        3000,   #27
                                        0,      #28
                                        0,      #29
                                        0,      #30
                                        0,      #31
                                        0,      #32
                                        0,      #33
                                        0,      #34
                                        0,      #35
                                        0,      #36
                                        0,      #37
                                        0,      #38
                                        0,      #39
                                        0,      #40
                                        3895,   #41
                                        425,    #42
                                        3895,   #43
                                        425,    #44
                                        3895,   #45   
                                        3895]}) #46     

    #input and choose packet version
    Version = int(export_values.iloc [0]['Values'])
    version_1 = version_1_base[['Position','Quantity','Price','Total price']]
    version_2 = version_2_base[['Position','Quantity','Price','Total price']]
    
    # choose 1+0 or 1+1 scenario:
    scenario = int(export_values.iloc [16]['Values'])
    if scenario == 2:
                    if Version == 1:
                        vers = version_1          
                    elif Version == 2:
                        vers = version_2
    elif scenario == 1:
                    if Version == 1:
                        vers = version_1.drop(labels = [1,3],axis = 0)   
                        vers.loc[vers['Quantity'] == 2, 'Quantity'] = 1
                        vers.loc[vers['Total price'] == 9280, 'Total price'] = 4640 
                    elif Version == 2:
                        vers = version_2.drop(labels = [1,3],axis = 0)
                        vers.loc[vers['Quantity'] == 4, 'Quantity'] = 2
                        vers.loc[vers['Total price'] == 31200, 'Total price'] = 15600
                        
    #input subs
    subs = int(export_values.iloc [1]['Values'])             # count subscribers
    #input additional positions
    add_enodeb = int(export_values.iloc [3]['Values'])       # add count of all eNodeB on prjct 
    add_nontelrad = int(export_values.iloc [4]['Values'])    # add non-Telrad enodeB count
    add_42u = int(export_values.iloc [5]['Values'])          # add 42U box count
    add_7ubox = int(export_values.iloc [6]['Values'])        # add 7U box count
    add_Router = int(export_values.iloc [7]['Values'])       # add Router count
    add_SGW = int(export_values.iloc [8]['Values'])          # add SGW count
    add_RGW = int(export_values.iloc [9]['Values'])          # add RGW count
    add_l2 = int(export_values.iloc [11]['Values'])          # add L2 service count
    add_sfp10 = int(export_values.iloc [10]['Values'])       # add SFP 10G+ count


    #Count of EPC , iHSS, iPCRF if subs < 650 : 
    if scenario == 2:
                        count_epc = ()
                        if np.array(int(math.ceil((subs-150)/50)*2)) < 1:  # EPC
                            count_epc = 2
                        else: 
                            count_epc  = np.array(int(math.ceil((subs-150)/50)*2))
                            
                        count_hss = ()                           # sub<650   iHSS
                        if np.array(int(math.ceil((subs-150)/50))) < 1:  
                            count_hss = 1
                        else: 
                            count_hss = np.array(int(math.ceil((subs-150)/50)))
                            
                        count_pcrf =  ()                         # sub<650   iPCRF
                        if np.array(int(math.ceil((subs-150)/50)*2)) < 1:  
                            count_pcrf = 2
                        else: 
                            count_pcrf = np.array(int(math.ceil((subs-150)/50)*2))
                        
                        #Count iHSS, iPCRF if 1000 > subs > 650 : 
                        count_hss_2 = np.array(int(math.ceil((subs-650)/50)))    # sub>650   iHSS
                        count_pcrf_2 = np.array(int(math.ceil((subs-650)/50)*2)) # sub>650   iPCRF
                        
                        #Count EPC, iHSS, iPCRF if subs > 1000 : 
                        count_epc_2_2 =  ()
                        if np.array(int(math.ceil((subs-1000)/50)*2)) < 1:      # EPC > 1000
                            count_epc_2_2 = 2
                        else: 
                            count_epc_2_2  = np.array(int(math.ceil((subs-1000)/50)*2))        
                        count_hss_2_2 = ()                            # sub>1000   iHSS 500
                        if np.array(int(math.ceil((subs-1000)/50))) < 1:  
                            count_hss_2_2 = 1
                        else: 
                            count_hss_2_2 = np.array(int(math.ceil((subs-1000)/50)))

                        count_pcrf_2_2 =  ()
                        if np.array(int(math.ceil((subs-1000)/50)*2)) < 1:      # sub>1000   iPCRF 500
                            count_pcrf_2_2 = 2
                        else: 
                            count_pcrf_2_2  = np.array(int(math.ceil((subs-1000)/50)*2))
                    
                        
    elif scenario == 1:
                        count_epc = ()
                        if np.array(int(math.ceil(subs-150)/50)) < 1:  # EPC
                            count_epc = 2
                        else: 
                            count_epc  = np.array(int(math.ceil(subs-150)/50))
                            
                        count_hss = ()                           # sub<650   iHSS
                        if np.array(int(math.ceil((subs-150)/50))) < 1:  
                            count_hss = 1
                        else: 
                            count_hss = np.array(int(math.ceil((subs-150)/50)))
                            
                        count_pcrf =  ()                         # sub<650   iPCRF
                        if np.array(int(math.ceil(subs-150)/50)) < 1:  
                            count_pcrf = 2
                        else: 
                            count_pcrf = np.array(int(math.ceil(subs-150)/50))
                        
                        #Count iHSS, iPCRF if 1000 > subs > 650 : 
                        count_hss_2 = np.array(int(math.ceil((subs-650)/50)))    # sub>650   iHSS
                        count_pcrf_2 = np.array(int(math.ceil(subs-650)/50)) # sub>650   iPCRF
                        
                        #Count EPC, iHSS, iPCRF if subs > 1000 : 
                        count_epc_2_2 =  ()
                        if np.array(int(math.ceil(subs-1000)/50)) < 1:      # EPC > 1000
                            count_epc_2_2 = 2
                        else: 
                            count_epc_2_2  = np.array(int(math.ceil(subs-1000)/50))        
                        count_hss_2_2 = ()                            # sub>1000   iHSS 500
                        if np.array(int(math.ceil((subs-1000)/50))) < 1:  
                            count_hss_2_2 = 1
                        else: 
                            count_hss_2_2 = np.array(int(math.ceil((subs-1000)/50)))

                        count_pcrf_2_2 =  ()
                        if np.array(int(math.ceil(subs-1000)/50)) < 1:      # sub>1000   iPCRF 500
                            count_pcrf_2_2 = 2
                        else: 
                            count_pcrf_2_2  = np.array(int(math.ceil(subs-1000)/50))

    #additionals licences and HW:
    less_150 = pd.DataFrame([
                    {'Position': "Additional licences not need",'Quantity': '','Price': '', 'Total price': 0}
                    ])

    subs_1000 = pd.DataFrame([
                    {'Position': "Additional licences not need",'Quantity': '','Price': '', 'Total price': 0}
                    ])

    less_650 = pd.DataFrame([
                    {'Position': Position[0],'Quantity': count_epc,'Price': additional['Price'][0], 'Total price': count_epc*additional['Price'][0]},
                    {'Position': Position[1],'Quantity': count_hss,'Price': additional['Price'][1], 'Total price': count_hss*additional['Price'][1]},
                    {'Position': Position[2],'Quantity': count_pcrf,'Price': additional['Price'][2], 'Total price': count_pcrf*additional['Price'][2]}
                    ])

    subs_650 = pd.DataFrame([
                    {'Position': Position[0],'Quantity': count_epc,'Price': additional['Price'][0], 'Total price': count_epc*additional['Price'][0]},
                    {'Position': Position[5],'Quantity': 1,'Price': additional['Price'][5], 'Total price': additional['Price'][5]},
                    {'Position': Position[6],'Quantity': 2,'Price': additional['Price'][6], 'Total price': (additional['Price'][6]*2)}
                    ])

    subs_650_1000 = pd.DataFrame([
                    {'Position': Position[0],'Quantity': count_epc,'Price': additional['Price'][0], 'Total price': count_epc*additional['Price'][0]},
                    {'Position': Position[5],'Quantity': 1,'Price': additional['Price'][5], 'Total price': additional['Price'][5]},
                    {'Position': Position[1],'Quantity': count_hss_2,'Price': additional['Price'][1], 'Total price': count_hss_2*additional['Price'][1]},
                    {'Position': Position[6],'Quantity': 2,'Price': additional['Price'][6], 'Total price': (additional['Price'][6]*2)},
                    {'Position': Position[2],'Quantity': count_pcrf_2,'Price': additional['Price'][2], 'Total price': count_pcrf_2*additional['Price'][2]}
                    ])

    subs_1000_1500 = pd.DataFrame([
                    {'Position': Position[0],'Quantity': count_epc_2_2, 'Price': additional['Price'][0], 'Total price': count_epc_2_2*additional['Price'][0]},
                    {'Position': Position[1],'Quantity': count_hss_2_2, 'Price': additional['Price'][1], 'Total price': count_hss_2_2*additional['Price'][1]},
                    {'Position': Position[2],'Quantity': count_pcrf_2_2,'Price': additional['Price'][2], 'Total price': count_pcrf_2_2*additional['Price'][2]}
                    ])

    subs_1500 = pd.DataFrame([
                    {'Position': Position[0],'Quantity': count_epc_2_2, 'Price': additional['Price'][0], 'Total price': count_epc_2_2*additional['Price'][0]},
                    {'Position': Position[5],'Quantity': 1, 'Price': additional['Price'][5], 'Total price': additional['Price'][5]},
                    {'Position': Position[6],'Quantity': 2,'Price': additional['Price'][6], 'Total price': (additional['Price'][6]*2)}  
                    ])  

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
                addi = 'Need to check versions'
                
    #Additionals HW+SW equipment:
    #Poc server count
    server_POC = export_values.iloc [2]['Values']
    server_POC_final = ()
    if  server_POC == "RONET 300":
        if subs <= 300:
            server_POC_final = "RONET Compact pro 300"
            price_poc = additional['Price'][16]
            count_poc = 1
            totalprice_poc = count_poc*price_poc
        else:
            server_POC_final = "Check Subs qnty"
            price_poc = "-"
            count_poc = "-"
            totalprice_poc = 0
    elif server_POC == "RONET 500":
        if subs <= 500:
            server_POC_final = "RONET Compact pro 500"
            price_poc = additional['Price'][17]
            count_poc = 1
            totalprice_poc = price_poc*count_poc
        else:
            server_POC_final = "Check Subs qnty"
            price_poc = "-"
            count_poc = "-"
            totalprice_poc = 0
    elif server_POC == "RONET Professional":
        server_POC_final = "RONET Profeccional pack:"
        price_poc = "-"
        count_poc = "-"
        totalprice_poc = 0
    
    #RONET PROFESSIONAL - HW+SW + additional licences:
    count_ronet_profi = ()
    server_POC_1 = export_values.iloc [2]['Values']
    if server_POC_1 == "RONET Professional":
        if (subs - 300) <= 0:
            count_ronet_profi = 0
        else:
            count_ronet_profi = np.array(int(math.ceil((subs - 300)/100)))
    else:
        count_ronet_profi = 0
        
    Ronet_Profi = pd.DataFrame([
        {'Position': 'RONET Professional HW', 'Quantity': '1', 'Price': additional['Price'][23], 'Total price': additional['Price'][23]},
        {'Position': 'RPV-20000-100 (SW +300 subs)', 'Quantity': '1', 'Price': additional['Price'][22], 'Total price': additional['Price'][22]},
        {'Position': 'Ronet Professional add licences (+100 subs)', 'Quantity': count_ronet_profi, 'Price': additional['Price'][24], 'Total price': count_ronet_profi*additional['Price'][24]}
        ])
    
    Ronet_Profi_final = ()
    server_POC_2 = export_values.iloc [2]['Values']
    if server_POC_2 == "RONET Professional":
        Ronet_Profi_final = Ronet_Profi
    else:
        Ronet_Profi_final = pd.DataFrame([
            {'Position': '-', 'Quantity': '-', 'Price': '-', 'Total price': 0}]) 
    
     #Make final Dataframe based on Server POC:
    Server_POC_final = pd.DataFrame([{'Position': server_POC_final, 'Quantity': count_poc, 'Price': price_poc, 'Total price': totalprice_poc}])    
    
    Ronet_server = pd.concat([Server_POC_final,Ronet_Profi_final],sort= False, axis=0)

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
            mars_nms_lic_1 = "-"
            price_mars_nms_lic_5 = additional['Price'][11]
            price_mars_nms_lic_1 = "-"
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

    #BTS tables:
    bts = int(export_values.iloc [12]['Values'])
    bts_type = export_values.iloc [13]['Values']
    
    bts_cnt = ()
    if bts <= 0:
        bts_cnt = ""
    else: bts_cnt = bts
    
    bts_df = pd.DataFrame([
        {'Position': bts_type, 'Quantity': bts_cnt, 'Price': 1, 'Total price': bts*1}])

    
    #terminals tables:
    terminals = int(export_values.iloc [14]['Values'])
    terminals_type = export_values.iloc [15]['Values']
    
    terminals_cnt = ()
    if terminals <= 0:
        terminals_cnt = ""
    else: terminals_cnt = terminals
    
    terminals_df = pd.DataFrame([
        {'Position': terminals_type, 'Quantity': terminals_cnt, 'Price': 1, 'Total price': terminals*1}])
    
    
           
    #Null index's in DataFrame - for beauty view.
    #add summary $ for block
    scenario_title = ()
    if scenario == 1:
        scenario_title = "1+0"
    elif scenario == 2:
        scenario_title = "1+1"
        
    title_1 = pd.DataFrame([
        {'Position': 'Scenario: ', 'Quantity': scenario_title, 'Price': '', 'Total price': 0},
        {'Position': 'Core Packet: #', 'Quantity': Version, 'Price': '', 'Total price': 0},])
    title_1.style.apply('font-weight: bold')

    title_2 = pd.DataFrame([
        {'Position': '', 'Quantity': '', 'Price': 'Totally for Core packet:', 'Total price': vers['Total price'].sum()},
        {'Position': '', 'Quantity': '', 'Price': '', 'Total price': 0},
        {'Position': 'Additional Core licences: ', 'Quantity': '', 'Price': '', 'Total price': 0}]) 

    title_3 = pd.DataFrame([
        {'Position': '', 'Quantity': '', 'Price': 'Totally for Additional licences:', 'Total price': addi['Total price'].sum()},
        {'Position': '', 'Quantity': '', 'Price': '', 'Total price': 0},
        {'Position': 'Server PoC:', 'Quantity': '', 'Price': '', 'Total price': 0}]) 
    
    title_4 = pd.DataFrame([
        {'Position': '', 'Quantity': '', 'Price': 'Totally for server PoC:', 'Total price': Ronet_server['Total price'].sum()},
        {'Position': '', 'Quantity': '', 'Price': '', 'Total price': 0},
        {'Position': 'Additional HW+SW equipment: ', 'Quantity': '', 'Price': '', 'Total price': 0}]) 
    
    total_hw_sw = pd.DataFrame([
        {'Position': '', 'Quantity': '', 'Price': 'Totally for additional HW and SW:', 'Total price': hw_sw['Total price'].sum()}]) 
    
    title_5 = pd.DataFrame([
        {'Position': '', 'Quantity': '', 'Price': '', 'Total price': 0},
        {'Position': 'BTS:', 'Quantity': '', 'Price': '', 'Total price': 0}]) 
    
    title_6 = pd.DataFrame([
        {'Position': '', 'Quantity': '', 'Price': '', 'Total price': 0},
        {'Position': 'Terminals:', 'Quantity': '', 'Price': '', 'Total price': 0}]) 
    
    title__null = pd.DataFrame([
        {'Position': '', 'Quantity': '', 'Price': '', 'Total price': 0},
        {'Position': '', 'Quantity': '', 'Price': '', 'Total price': 0}]) 
    
    total_bts_df = pd.DataFrame([
        {'Position': '', 'Quantity': '', 'Price': 'Totally for BTS:', 'Total price': bts_df['Total price'].sum()}]) 
    
    total_terminals_df = pd.DataFrame([
        {'Position': '', 'Quantity': '', 'Price': 'Totally for Terminals:', 'Total price': terminals_df['Total price'].sum()}])
    
    #Make tables with titels
    KP_total = pd.concat([title_1,vers,
                          title_2,addi,
                          title_3,Ronet_server,
                          title_4,hw_sw,total_hw_sw,
                          title_5,bts_df,total_bts_df,
                          title_6,terminals_df,total_terminals_df,
                          title__null]
                         ,sort= False, axis=0)
    
    #make tables without titles, for calculating SUM
    KP_calc  = pd.concat([vers,
                          addi,
                          Ronet_server,
                          bts_df,
                          terminals_df,
                          hw_sw],sort= False, axis=0).fillna(0)

    #Calculate Total price for all quantity in column:
    total = pd.DataFrame([
        {'Position': '', 'Quantity': '', 'Price': '', 'Total price': ''},
        {'Position': '', 'Quantity': '', 'Price': '', 'Total price': ''},
        {'Position': '', 'Quantity': '', 'Price': 'Project total price: ', 'Total price': KP_calc['Total price'].sum()}]) 

    #Make table Total + Main
    KP_calc_final = pd.concat([KP_total,total],sort= False, axis=0)
    KP_calc_final.loc[KP_calc_final['Total price'] == 0, 'Total price'] = ""

    writer = pd.ExcelWriter('media/results.xlsx')   # create excel writer object
    KP_calc_final.to_excel(writer)                  # write dataframe to excel 
    writer.save()                                   # save the excel 
    
    #transform DataFrame in Table 
    html_KP_calc = pretty_html_table.build_table(KP_calc_final
                                                    ,'blue_light'
                                                    , font_size='medium'
                                                    , text_align='left'
                                                    , width='auto'
                                                    , index=False)

    #write html to file 
    text_file = open("main/templates/show_result_calc.html", "w") 
    text_file.write(html_KP_calc)  
    text_file.close()
    
    



    


