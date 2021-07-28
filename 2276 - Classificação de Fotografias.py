def ehParaImprimir(psnr, enquadramento, exposicao):
    if(psnr > 80):
        if(enquadramento == "excelente" or enquadramento == "bom"):
            if(exposicao == "bem exposta"):
                return True
    return False

def ehBoa(psnr, enquadramento, exposicao):
    if(psnr>=50 and psnr <= 80):
        if(enquadramento == "excelente"):
            if(exposicao == "bem exposta"):
                return True
    if(psnr >= 80):
        if(enquadramento == "excelente" or enquadramento == "bom"):
            if(exposicao == "subexposta" or exposicao == "superexposta"):
                return True
    return False

def ehMarromeno(psnr, enquadramento, exposicao):
    if(psnr < 50):
        if(enquadramento == "excelente"):
            if(exposicao == "bem exposta"):
                return True
    elif(psnr < 80):
        if(not ehBoa(psnr, enquadramento, exposicao)):
            return True
    elif((not ehBoa(psnr, enquadramento, exposicao)) and
            (not ehParaImprimir(psnr, enquadramento, exposicao))):
        return True
    return False

psnr = int(input())
enquadramento = input()
exposicao = input()

if(ehParaImprimir(psnr, enquadramento, exposicao)):
    print("para imprimir")
elif(ehBoa(psnr, enquadramento, exposicao)):
    print("boa")
elif(ehMarromeno(psnr, enquadramento, exposicao)):
    print("marromeno")
else:
    print("lixo")
