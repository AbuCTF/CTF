from Crypto.Util.number import long_to_bytes

# Given parameters
e = 3

# RSA decryption function
def rsa_decrypt(ct, n, e):
    pt = pow(ct, (1/e), n)
    return pt

# RSA parameters and ciphertexts
n1 = 96137714481560340073780038250015316564930752333880363375193088083653975552334517899735106334409092229494004991796910602440032630762575914714152238916128674595912438177270978040111855327624812652948702562503276973409716595778936978757384935820012322432156169815110042972411989274515686945691887468406312791931
ct1 = 45640508926729498938915879450220374487095109122207451961200230820161694723491945276893630019713859109920025191680053056485030809079137883906737197875968862878423820820515399840094772412319820062860149582361429346029277273870654355752499436360499181221418835401103925420623212341317366954144592892392013649421
n2 = 90990790933807553440094447797505116528289571569256574363585309090304380702927241663491819956599368816997683603352289726407304960362149545383683196526764288524742203975596414405902155486632888712453606841629050125783639571606440840246928825545860143096340538904060826483178577619093666337611264852255012241011
ct2 = 58149644956871439128498229750735120049939213159976216414725780828349070974351356297226894029560865402164610877553706310307735037479690463594397903663323983980128060190648604447657636452565715178438939334318494616246072096228912870579093620604596752844583453865894005036516299903524382604570097012992290786402
n3 = 86223965871064436340735834556059627182534224217231808576284808010466364412704836149817574186647031512768701943310184993378236691990480428328117673064942878770269493388776005967773324771885109757090215809598845563135795831857972778498394289917587876390109949975194987996902591291672194435711308385660176310561
ct3 = 16168828246411344105159374934034075195568461748685081608380235707338908077276221477034184557590734407998991183114724523494790646697027318500705309235429037934125253625837179003478944984233647083364969403257234704649027075136139224424896295334075272153594459752240304700899700185954651799042218888117178057955

# Decrypt the ciphertexts
plaintext1 = rsa_decrypt(ct1, n1, e)
plaintext2 = rsa_decrypt(ct2, n2, e)
plaintext3 = rsa_decrypt(ct3, n3, e)

# Convert the plaintexts from float to integer
plaintext1 = int(plaintext1)
plaintext2 = int(plaintext2)
plaintext3 = int(plaintext3)

# Convert the decrypted plaintexts from long integer to bytes
decrypted1 = long_to_bytes(plaintext1)
decrypted2 = long_to_bytes(plaintext2)
decrypted3 = long_to_bytes(plaintext3)

# Print the decrypted plaintexts
print("Decrypted plaintext 1:", decrypted1)
print("Decrypted plaintext 2:", decrypted2)
print("Decrypted plaintext 3:", decrypted3)