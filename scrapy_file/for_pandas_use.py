import PyPDF2
import pandas as pd
import csv
pd.set_option('display.max_rows', 500)
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)
# A.R.A. International (Reg: 50),Anowarul Bashir Khan,Managing Partner,"ARA Bhaban (1st Fl), 39, Kazi Nazrul Islam ",Avenue,"Kawran Bazar, Dhaka","Tel: 8112148, 8118254, 01911323622",Email: info@ara-intl.com,Abid Export Ltd. (Reg: 747),Didarul Alam,Managing Director,"House # 82/A, New Airport Road","Banani, Dhaka","Tel: 8821975, 01552152091",Email: abidexport@gmail.com,Ahnaf Fashions Limited (Reg: 1391),Md. Monjurul Islam,Managing Director,"House # 272 (2nd Fl), Road # 13, Lake Road, ",New DOHS,"Mohakhali, Dhaka","Tel: 9893108, 01711547161",Email: monju@jmintlbd.com,Akil Fashion (Reg: 1271),Md.Ali Azam Sarker,Proprietor,"House # 15, Road #17, Sector # 07","Uttara, Dhaka","Tel: 8953915, 01819213248",Email: akilfashionbd@yahoo.com,Al Aseel Fashions (Pvt.) Ltd. (Reg: 662),Mohammad Salauddin,Managing Director,"Notun Sonakanda Bus Stand, Rohitpur, ",Keranigonj Model Town,"Keranigonj, Dhaka",Tel: 01817-119588 01768613393,Email: shafinahammed83@gmail.com,Allure Sourcing Limited (Reg: 1459),Mohammad Kamrul Islam Chowdhury,Managing Director,"Plot # CWN(A)11/A, Concord Baksh Tower(6th ","Fl), Road # 48","Gulshan-2, Dhaka","Tel: +880966719719, 01711595956",Email: rajibkislam@alluresourcing.com,Amann Bangladesh Ltd. (Reg: 1264),Shafiquz Zaman,Managing Director,"Civil Sarwar Complex, Plot # 42/A, Road #17, ",Sector # 14,"Uttara, Dhaka","Tel: 7914934-37, 01847027000",Email: shafiq.zaman@ammann.com,Ambience Denim Limited (Reg: 1485),S M Mijahidul Islam,Managing Director,"House # 20, Road # 13, Sector # 14","Uttara, Dhaka","Tel: 02-94469966, 01710-486992",Email: info@ambiencedenimltd.com,Amial Corporation (Reg: 1442),Shah Jamal Mostafa,Proprietor,Park Plaza (S,-,"5), House # 31, Road # 17","Banani, Dhaka","Tel: 02-9821858, 01732770020",Email: amialintl@gmail.com,Apex International (Reg: 1412),Dr. Sujauddin Ahmed Sujan,Managing Director,"39, MM Ali Road, Lalkhan Bazar","Khulshi, Chittagong","Tel: 01731894658, 01811503537",Email: sujon77@gmail.com,Aphrodite Design Link Ltd. (Reg: 1166),Kazi Abdullah Al Masum,Managing Director,"House # 40 (3rd Floor), Road # 13, Sector # 4","Uttara, Dhaka","Tel: 01711815601, 8913863",Email: masum@aphrodite-design.com,Apparel Gallery (Reg: 1036),Mohammad Jahirul Haque Bhuiyan,Proprietor,"House # 1 (1st Floor), Road # 2/E, Sector # 4","Uttara, Dhaka","Tel: 01713017776, 8951492",Email: jahir@apparelgallerybd.com,Apparel Soucing (HK) Ltd. (Reg: 1396),Rubina Yasmin,Managing Director,"House # 381, Road # 6, Dhaka Cantonment","Baridhara DOHS, Dhaka",Tel: 01713149512,Email: iqbal@pathiotjnoupbd.com,Apparel.com Limited (Reg: 1373),Md. Jahangir Hossain,Managing Director & CEO,"Mustafa Arcade, Flat # A4, Block ",-,"J, Road # ","1/A, House #18","Baridhara, Dhaka",Tel: 01713 369086,Email: jahangir@appareldotcomlimited.com,Apparelopolis Ltd. (Reg: 1418),Md. Riaz Uz Zaman,Managing Director,"Flat # C2, Plot # 287, Road # 4","Mirpur DOHS, Dhaka","Tel: 51040091, 01740554885",Email: info@apparelopolis.net,Aqua Sourcing Ltd. (Reg: 1309),Md. Zillur Rahman Mirdha,Managing Director,"Plot # 15, Siam Tower (12th Floor), Sector # 03","Uttara, Dhaka",Tel: 01711595929,Email: ,Ariyad Fashions Ltd. (Reg: 1432),Kazi Md. Mofizul Hoque,Managing Director,"Dhanshiri, Flat",-,"B5, Plot # 297/298, Shadinata ",Sarani Rd,"Uttar Badda, Dhaka","Tel: 01973006868, 01939377325",Email: ariyadfashionsltd@yahoo.com,Asia Excel Trading Ltd. (Reg: 788),Ravin Shah,General Manager,"Crystal Palace (7th Flr.) ,House # SE (D) 22 ","(New), Road # 140","Gulshan-1, Dhaka","Tel: 01613013865, 9889931",Email: ravin@indochinebd.com
with open('bgmea.csv', 'r') as file:
    csv_reader = csv.reader(file)
    for l in csv_reader:
        print("line", l[0:8],l[8:16],l[16:24],l[24:64], l[32:],l[40:],l[48:])









