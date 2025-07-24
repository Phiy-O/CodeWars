function skiponacci(n) {
    let fibArr = [0, 1]
    let res = []
    for (let x = 2;x <= n;x++){
        fibArr.push(fibArr[fibArr.length - 1] + fibArr[fibArr.length - 2])
    }
    for (let i = 1; i < fibArr.length; i++){
        if (i % 2 != 0){
            res.push(fibArr[i].toString())
        } else {
          res.push("skip")
        }
    }
    return res.join(" ")
}
