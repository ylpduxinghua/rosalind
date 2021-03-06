#local alignment Smith-Waterman

s="""
PSKNFWSPTEWAESREMSHQCYTFTKKAFEPFAANDRCENPDMPHWAKLPVYEYGVWKIP
EKLNGKSKSMSHVNYFLFGNMWTFTVNGNTRIDMSCLKYLREDERYWEDESNSGMCQMYL
KYLIYIKPTRWMGNMYVPDWTGNNVGFDDITIHGVFAIVIKVRGFNWCQFGQPYVEKRYC
SEMTTRGWWPHNMQYLWYDMLYSGMDTEYTQGEWPHHEAYRYFWRFQSKERCFENVWPCS
QVWLSYSCSFAWKECTCNQKTDFHIMESGTDQYWSSPAIWVWVYVHMPPYRTEGQKKFEE
PDHYGCGQMGYWTAAWKCKSQWRNCPQIEVWYGRMSILIRRFKVPRCAFTPEFRPAIRYV
HHTDHTQNRTIKARCANVYECHHMEMRHRKHTATSACSLRSNDTMANMWIYIGDYIMGAA
HRQVDNFIGDDIMALIIPVQFQVCQRCSGGTPQWTPDWYGAHEPDEVCAHYTWANLQFPP
NNIIQGWRHGIKLHRYIWWLRRHQHHKHYMKCWPVAYNTEMLHLDLSKPAATMWIMEAGL
EPIMDGQCMELWFTVQFDLVPQYVPYEWWRNVYMVVIFHQDMAFCDIMGSPMPMWEDAKC
RYTINQCDVKTPLHVTQRCAHLTTPMTQELLHFTHSGHYGMPAAPWTDSASPKKTVDVWQ
AYLSHHYDALEEISNCAQCVKHNYMLPDSVDYLFCKYQIGETIQRPCWWIQPDLCHMPMT
QPFWGTPEAESNDKEAIAVMHCAIVWRVTIDMMMSLSFMTYRNADELWCLSHAWVYGHNT
YKMSWMGDQDTLCSHRPPASICDENWYMKNQNGDYPVTRGWRGCKPECTFFTKGTVMPAM
TDWDKARDPILQEYVKIMKWRWWYVTNIWAIWKKEFMNTKKFNVHAHAKDCWMYNGQQGN
"""
t="""
HNSRWNHEDLAEPYRAFYKQELNFTYKSRNGCSKHDGDWRSWTSTWWASGGGTVYQQRET
SCVMNNIDNVFFFKNLNCNHTNCNKDTWYDNNKAGKEEWYIWAVAPHITFKYNHQGCKRC
RIIHQHSAPYPTRTCQGIFHMICAQCCEPRQSHMAFDQTANNYSGMVLYSDGWEIPVEYV
DIKSTESDKINSSFYQESNFACGIHEFMVHGPEMGWPKYGWSPRKSMKNQNKSWRWIGHW
YNDFHRYVHGWHTPTATSTCNLSGSKYPIWRQPAQDTGCQQMGYWTRMNSIAQIAYKKDW
KCWLADMCKSQWRNCPQIEVWYVFMSGQIRRFKVPRCAFTPTWMYFEFRPAIRYVHHTAH
TANVYKCHHHRKHTATSACSLRSNDTLNTLIDSTGDYIMGSASFQLKHRQVPLDNFIGYD
DMALIIGVQFQVCQRCSGGTTPDWYGAHEPYCVCAGYTWANLSSTVFKPPNNIYQGWRHG
IKIRHVVPTNHPYIIRQIHQPMLRRTQKQHHKHYMKCGPVAYNTWMLHLDLSKEHKEDME
MGLEPIMKGQCRKMVQIKKVPQYVPPEWWVIFHDMAFCMGYGHKDCESTLGAWEDAKCRC
CTRTLWKENQDNQPLHVNKIGVGRVVQRCAHLGPPMEQELFMAPYRQFNSIKEPVPEDVC
FRTWGKKCILAEALEGENGPFAGKETFHWHRRLMQTWCFTFDVSWNMQWRIGSVFQALYC
HGDCPQHMACTCSHNQNPWNMKARCSGKFQFNTHHMDMQPHTWPRGKDNLWTDSIYQNHR
HYDAQAFQYMFIGNLYEKPLEACHNYGVQYYHIQFHVKKVTWQVFSTSDDGVYKWLPDNE
TAQHITSSTILNLCWMHSRQEDEQCSFRATIDHYQMYEPDLCWKRRARAQVMDCTKDRPR
GHHLWTAFQVALEFCCTHEKNSAESEVRYAEPNSDQNTMDPEVTPVTKVAR
"""

def local_alignment(s,t):
    s=s.replace("\n","")
    t=t.replace("\n","")
    
    import pandas as pd
    PAM250=pd.DataFrame([
        [2, -2, 0, 0, -3, 1, -1, -1, -1, -2, -1, 0, 1, 0, -2, 1, 1, 0, -6, -3],
        [-2, 12, -5, -5, -4, -3, -3, -2, -5, -6, -5, -4, -3, -5, -4, 0, -2, -2, -8, 0],
        [0, -5, 4, 3, -6, 1, 1, -2, 0, -4, -3, 2, -1, 2, -1, 0, 0, -2, -7, -4],
        [0, -5, 3, 4, -5, 0, 1, -2, 0, -3, -2, 1, -1, 2, -1, 0, 0, -2, -7, -4],
        [-3, -4, -6, -5, 9, -5, -2, 1, -5, 2, 0, -3, -5, -5, -4, -3, -3, -1, 0, 7],
        [1, -3, 1, 0, -5, 5, -2, -3, -2, -4, -3, 0, 0, -1, -3, 1, 0, -1, -7, -5],
        [-1, -3, 1, 1, -2, -2, 6, -2, 0, -2, -2, 2, 0, 3, 2, -1, -1, -2, -3, 0],
        [-1, -2, -2, -2, 1, -3, -2, 5, -2, 2, 2, -2, -2, -2, -2, -1, 0, 4, -5, -1],
        [-1, -5, 0, 0, -5, -2, 0, -2, 5, -3, 0, 1, -1, 1, 3, 0, 0, -2, -3, -4],
        [-2, -6, -4, -3, 2, -4, -2, 2, -3, 6, 4, -3, -3, -2, -3, -3, -2, 2, -2, -1],
        [-1, -5, -3, -2, 0, -3, -2, 2, 0, 4, 6, -2, -2, -1, 0, -2, -1, 2, -4, -2],
        [0, -4, 2, 1, -3, 0, 2, -2, 1, -3, -2, 2, 0, 1, 0, 1, 0, -2, -4, -2],
        [1, -3, -1, -1, -5, 0, 0, -2, -1, -3, -2, 0, 6, 0, 0, 1, 0, -1, -6, -5],
        [0, -5, 2, 2, -5, -1, 3, -2, 1, -2, -1, 1, 0, 4, 1, -1, -1, -2, -5, -4],
        [-2, -4, -1, -1, -4, -3, 2, -2, 3, -3, 0, 0, 0, 1, 6, 0, -1, -2, 2, -4],
        [1, 0, 0, 0, -3, 1, -1, -1, 0, -3, -2, 1, 1, -1, 0, 2, 1, -1, -2, -3],
        [1, -2, 0, 0, -3, 0, -1, 0, 0, -2, -1, 0, 0, -1, -1, 1, 3, 0, -5, -3],
        [0, -2, -2, -2, -1, -1, -2, 4, -2, 2, 2, -2, -1, -2, -2, -1, 0, 4, -6, -2],
        [-6, -8, -7, -7, 0, -7, -3, -5, -3, -2, -4, -4, -6, -5, 2, -2, -5, -6, 17, 0],
        [-3, 0, -4, -4, 7, -5, 0, -1, -4, -1, -2, -2, -5, -4, -4, -3, -3, -2, 0, 10]],        
        index=['A', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'K', 'L', 'M', 'N', 'P', 'Q', 'R', 'S', 'T', 'V', 'W', 'Y'],
        columns=['A', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'K', 'L', 'M', 'N', 'P', 'Q', 'R', 'S', 'T', 'V', 'W', 'Y'])
    
    dp=[[0 for j in range(len(t) + 1)] for i in range(len(s) + 1)]
    maximum=0
    s_start=0
    t_start=0
    
    for i in range(1, len(s)+1):
        for j in range(1,len(t)+1):
            cost=PAM250[s[i-1]][t[j-1]] 
            dp[i][j] = max(0,dp[i-1][j]-5 , dp[i][j-1]-5 , dp[i-1][j-1] + cost) #Smith-watermanの場合、スコアが負にならない
    
            if dp[i][j]>maximum:
                maximum=dp[i][j]
                s_start=i
                t_start=j

    s_align=''
    t_align=''
    i=s_start
    j=t_start
    #Begin with the highest score, end when 0 is encountered
    while (i>0 and j>0):
        if dp[i][j] ==dp[i-1][j-1]+PAM250[s[i-1]][t[j-1]]:
            s_align += s[i-1]
            t_align += t[j-1]
            i -= 1
            j -= 1
        elif i>0 and dp[i][j]==dp[i-1][j]-5:
            s_align += s[i-1]
            i -=1
        elif j>0 and dp[i][j]==dp[i][j-1]-5:
            t_align += t[j-1]
            j -= 1
        elif dp[i][j]==0:
            break

    print(maximum)
    print(s_align[::-1])
    print(t_align[::-1])

local_alignment(s,t)
