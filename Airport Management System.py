import pandas as pd
Dates = ['01/10/2025','01/10/2025','01/10/2025','01/10/2025','02/10/2025','02/10/2025','02/10/2025','03/10/2025','03/10/2025','03/10/2025','03/10/2025','04/102025','04/102025','05/10/2025','05/10/2025',
         '05/10/2025']
Columns = ['Airline','Departure','Arrival','Stops','Time of Departure','ETA','Duration','Capacity','Vacancy','List of PNR']
pd.set_option('display.max_columns',None)
PNR1 = []
for i in range(1,149):
    i2=f"{i:03d}"
    PNR1.append('INBK'+i2)
PNR2 = []
for i in range(1,139):
    i2=f"{i:03d}"
    PNR2.append('AIBD'+i2)
PNR3 = []
for i in range(1,116):
    i2=f"{i:03d}"
    PNR3.append('AIPB'+i2)

PNR4 = []
for i in range(1,86):
    i2=f"{i:03d}"
    PNR4.append('INDB'+i2)
PNR5 = []
for i in range(1,81):
    i2=f"{i:03d}"
    PNR5.append('AIBD'+i2)
PNR6 = []
for i in range(1,127):
    i2=f"{i:03d}"
    PNR6.append('INPB'+i2)
PNR7 = []
for i in range(1,122):
    i2=f"{i:03d}"
    PNR7.append('INDB'+i2)
PNR8 = []
for i in range(1,139):
    i2=f"{i:03d}"
    PNR8.append('INBK'+i2)
PNR9 = []
for i in range(1,75):
    i2=f"{i:03d}"
    PNR9.append('AIBD'+i2)
PNR10 = []
for i in range(1,70):
    i2=f"{i:03d}"
    PNR10.append('AIDB'+i2)
PNR11 = []
for i in range(1,111):
    i2=f"{i:03d}"
    PNR11.append('AIKB'+i2)
PNR12 = []
for i in range(1,130):
    i2=f"{i:03d}"
    PNR12.append('INBD'+i2)
PNR122 = []
for i in range(1,129):
    i2=f"{i:03d}"
    PNR122.append('AIPB'+i2)
PNR13 = []
for i in range(1,96):
    i2=f"{i:03d}"
    PNR13.append('AIKB'+i2)
PNR14 = []
for i in range(1,109):
    i2=f"{i:03d}"
    PNR14.append('INDB'+i2)
PNR15 = []
for i in range(1,118):
    i2=f"{i:03d}"
    PNR15.append('INPB'+i2)
R1 = ['Indigo','Bokaro','Kolkata','Non-Stop','11:10      ','11:55','45min',150,2,PNR1]
R2 = ['Air Inida','Bokaro','Delhi','1 Stop','12:40      ','17:45','5h      ',150,12,PNR2]
R3 = ['Air India','Patna','Bokaro','Non-Stop','18:25      ','17:25','1h      ',120,5,PNR3]
R4 = ['Indigo','Delhi','Bokaro','1 Stop','17:15      ','20:35','3h 30min',100,15,PNR4]
R5 = ['Air India','Bokaro','Delhi','1 Stop','09:10      ','16:45','7h 35min',100,20,PNR5]
R6 = ['Indigo','Patna','Bokaro','Non-Stop','12:25      ','13:10','45min',130,4,PNR6]
R7 = ['Indigo','Delhi','Bokaro','Non-Stop','13:15      ','14:40','1h 25min',130,9,PNR7]
R8 = ['Indigo','Bokaro','Kolkata','1 Stop','08:45      ','12:25','3h 40min',150,12,PNR8]
R9 = ['Air India','Bokaro','Delhi','1 Stop','12:40      ','20:50','8h 10min',100,26,PNR9]
R10 = ['Air India','Delhi','Bokaro','1 Stop','13:15      ','21:05','7h 50min',100,31,PNR10]
R11 = ['Air India','Kolkata','Bokaro','Nom-Stop','20:25      ','21:05','40min',120,10,PNR11]
R12 = ['Indigo','Bokaro','Delhi','Non-Stop','09:45      ','11:20','1h 35min',140,11,PNR12]
R122 = ['Air India','Patna','Bokaro','Non-Stop','12:10      ','12:55','45min',140,12,PNR122]
R13 = ['Air India','Kolkata','Bokaro','Non-Stop','11:10      ','12:00','50min',110,15,PNR13]
R14 = ['Indigo','Delhi','Bokaro','1 Stop','12:45      ','19:10','6h 25min',130,22,PNR14]
R15 = ['Indigo','Patna','Bokaro','Non-Stop','18:25      ','19:10','45min',130,13,PNR15]
Flights = pd.DataFrame([R1,R2,R3,R4,R5,R6,R7,R8,R9,R10,R11,R12,R122,R13,R14,R15],index=range(1,17),columns=Columns)
Flights.insert(loc=0,column='Date',value=Dates)

h=1
while h>0:
    print(Flights.iloc[0:16,0:9])
    
    print('Note :-','If you want to book a ticket, PRESS B ','If you want to check youur flight detailts, PRESS D ','If you want to change your flight, PRESS CH ','If you want to cancel your flight, PRESS C',sep='\n')
    x=input('How can we help you? : ')

    if x=='B':
        D  = input(' Enter Date (DD/MM/YYYY) , Choose date between 01,10,2025 to 05/10/2025 : ')
        DE = input('From: ').capitalize()
        AR = input('To: ').capitalize()

        mask = (Flights['Date']==D) & (Flights['Departure']==DE) & (Flights['Arrival']==AR)
        if not mask.any():
            print('No flights available')
        else:
            idx = Flights[mask].index[0]
            new_pnr = 'NEW' + DE[0] + AR[0] + D[:2]
            Flights.at[idx,'List of PNR'].append(new_pnr)
            print('Ticket booked successfully. PNR:', new_pnr)

    elif x=='D':
        pnr=input('Enter your PNR no. : ')
        for i in range(16):
            if pnr in Flights.iat[i,10]:
                print(Flights.iloc[i,0:10])
                break
        else:
            print('Invalid PNR')
        
    elif x=='C':
        pnr = input('Enter your PNR no. ').strip()
        cancelled = False
        for row_pos, row in Flights.iterrows():
            pnrs = row['List of PNR']
            if isinstance(pnrs, list) and pnr in pnrs:
                pnrs.remove(pnr)
                Flights.at[row.name, 'List of PNR'] = pnrs
                print('Your ticket has been cancelled')
                cancelled = True
                break
        if not cancelled:
            print('Invalid PNR')
    elif x=='CH':
        pnr = input('Enter your PNR : ').strip()
        changed = False
        for row_pos, row in Flights.iterrows():
            pnrs = row['List of PNR']
            if isinstance(pnrs, list) and pnr in pnrs:
                pnrs.remove(pnr)
                Flights.at[row.name, 'List of PNR'] = pnrs
                print('Please enter the new flight details : ')
                D  = input(' Enter Date (DD/MM/YYYY) , Choose date between 01,10,2025 to 05/10/2025 : ')
                DE = input('From: ').capitalize()
                AR = input('To: ').capitalize()

                mask = (Flights['Date']==D) & (Flights['Departure']==DE) & (Flights['Arrival']==AR)
                if not mask.any():
                    print('No flights available')
                else:
                    idx = Flights[mask].index[0]
                    new_pnr = 'NEW' + DE[0] + AR[0] + D[:2]
                    Flights.at[idx,'List of PNR'].append(new_pnr)
                    print('Ticket booked successfully. PNR:', new_pnr)
                changed = True
                break
        if not changed:
            print('Invalid PNR')
       
    
        
            
    else:
        print('Please choose from the given options only : ')
    while True:
        end = input('Do you need any other help? (YES/NO) : ').strip().lower()
        if end in ('yes', 'y'):
            break
        elif end in ('no', 'n'):
            h = -1
            break
        else:
            print('Please answer YES or NO only.')
print('I am glad I could help you')