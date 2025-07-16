function vowelIndices(word){
  //your code here
    let arr = []
    let vow = ['a', 'i', 'u', 'e', 'o', 'y']
    for (let x = 0; x < word.length; x++){
        if (vow.includes(word[x].toLowerCase())) {
            arr.push(x + 1)
        }
    }
    return arr
}
