// so basicly in this kind of study case we must make our own function for execute a string
//Create reverse function for the String prototype
String.prototype.reverse = function() {
  let result = ''
  for (let x = this.length - 1; x >= 0; x--){
    result += this[x]
  }
  return result
}
