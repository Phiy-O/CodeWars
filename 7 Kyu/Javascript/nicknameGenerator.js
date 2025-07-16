function nicknameGenerator(name){
  //code goes here
  let arr = []
  let vow = ['a', 'i', 'u', 'e', 'o']
  if (name.length < 4) {
    return "Error: Name too short"
  }
  
  for (let x = 0; x < 3; x++) {
    if (name.length > 3) {
      arr.push(name[x])
    }
    if (x === 2 && vow.includes(name[x])) {
        arr.push(name[x+1])
    }
  }
  return arr.join("")
}
