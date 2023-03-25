from Crypto.Util.number import *
from gmpy2 import *

flag=open('dist/flag.txt','r').readline().strip()


#assert len(flag)==48
flag1=flag[0:8].encode()
flag2=flag[8:int(2*len(flag)/3)].encode()
flag3=flag[int(2*len(flag)/3):].encode()

print(flag1+flag2+flag3)


print("=====================================flag1")
m=bytes_to_long(flag1)
p=getPrime(64)
q=getPrime(64)
e=65537
n=p*q
c=powmod(m,e,n)
print("n =",n)
print("e =",e)
print("c =",c)



print("=====================================flag2")
m=bytes_to_long(flag2)
p=getPrime(1024)
q=next_prime(p)
e=65537
n=p*q
c=powmod(m,e,n)
print("n =",n)
print("e =",e)
print("c =",c)


print("=====================================flag3")
m=bytes_to_long(flag3)
p=getPrime(1024)
q=getPrime(1024)
e1=65537
e2=12345
n=p*q
c1=powmod(m,e1,n)
c2=powmod(m,e2,n)
print("n =",n)
print("e1 =",e1)
print("e2 =",e2)
print("c1 =",c1)
print("c2 =",c2)



'''

=====================================flag1
n = 266390013019452180606454446621936087871
e = 65537
c = 155813651375107551102251418069171209947
=====================================flag2
n = 25663792206416107064983043018758845103286254720419866201148346208388756908973665119150932825488179304190859724009783079121357673818313513048938684486823909211698403153772440009429027595295240814380639974245255778932775968036417515542166770892365066588080990741901766291447643288017117484089070078482250102237307694213095344315573112854993240893076379502076663811902885935075242996710087184837824700204135452768481953509169935317067270451080749081397642451521227732319171657526119801050268127934139248688696318471467663889665221898053059067170384924785390193066880482651275117947524692735155333311693999263691785388441
e = 65537
c = 19662419751049182688703099840706561872410108702815721980642342514045372374759068594817590891982419007138587105296139706786013541601821398926310969498608088975993207078467164024689541330491025190948115266510911650955016290881322910082496713693405102685058030898478064772881576156300905767606267214271932515473961365985150474552399787394398332408506865077417671555539574091868190369468284504719044973368421615343754859540763875419825753576140156405613243093177491437177083015265589464780827886779823358441066049525013281221509298400729492630828988452159569294941081965352947896178985173013436174312260079937606421510639
=====================================flag3
n = 22633347418572364534105672122631052383966382573582732236043098896149162862638296256562345291158532837003607390298269180042585525005265607927522063703727019571027350701439647125147857753826292927724403893958382139062806064676721296540788196204844834749814928729999519093309950782825029973177083617818632177236401456482423827159971492430997918952442602124722790429690566539756769782639334797310248530089345287211976934073087801623211392197933150829868149318178326906973836547896941872723176351240759500421864037880499239415778201615345335659434505864230912886565578384657827204325770099278027324733675064175011841079833
e1 = 65537
e2 = 12345
c1 = 4442378760405366496426229024642774716681583513263307314439871992034604142987718481232360007914288382346429886294791285215758411408008872866238640202479273838113226944317444809866737863158453801086399023013096962846766692978801971225444753847813072507847430341438502796635124040146940973655432036181240305757342726186085185182896488405115461721535944514023643305289197276211536734827716885644881294956806112971205108512654280175097238365503587429052953958976758126314025395523770412556245807365415669924038104934376033596389878351022643727460010358242357557084083469539051244739898558637840928363593187806233062312889
c2 = 22057525278891540609646550679999409552132518813106375432154804792554660595080890817429427651550196117542948966427472700934177034874433647906177833224193204019172236880537368909322965148174349243106361179427948451314800084405392350528710134040185206375971508302996556412622612274875028281881518472041337652119447917976437485693554362014371966184368864852491705497904670119802103824644064842146536412654411539518074016250811638302180625101000634845640116079558990244510876450063976001000338468055877834725834498160228297196848321048704946646085243596936563524034737387288959286194980720295927625300790961085614604291185

'''