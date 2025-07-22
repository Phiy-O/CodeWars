function i(word) {
  //.. 
  let vowCount = 0;
  let consonantCount = 0;
  for (let x of word){
    if ('aiueoAIUEO'.includes(x)){
      vowCount += 1
    } else {
      consonantCount += 1
    }
  }
  if (word === '' || /[a-z]/.test(word[0]) || 'iI'.includes(word[0]) || vowCount >= consonantCount){
    return 'Invalid word'
  }

  return 'i' + word
}
