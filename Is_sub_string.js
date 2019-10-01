let sub = 'abc';
let parent = 'a';

function findIndex(ch,startIndex,s){
	for(let i=startIndex;i<s.length;i++){
		if(ch == s.charAt(i)){
			return i;
		}
	}
	return -1;
}

function isSubString(index,subString,pString){
  if(subString.length > pString.length){
    return false;
  }
  const startIndex = findIndex(subString.charAt(0),index,pString);
  if(startIndex === -1){
    return false;
  } 
  let sStringI = 1;
  let pStringI = startIndex + 1;
  while(pStringI < pString.length){
    if(sStringI === subString.length){
      return true;
    }
    if(pString.charAt(pStringI) !== subString.charAt(sStringI)){
      return isSubString(pStringI+1,subString,pString);
    }
    sStringI++;
    pStringI++;
  }
  return true;
}

console.log(isSubString(0,'s','abc'))
console.log(isSubString(0,'a','abc'))
console.log(isSubString(0,'b','abc'))
console.log(isSubString(0,'c','abc'))
console.log(isSubString(0,'ab','abc'))
console.log(isSubString(0,'bc','abc'))
console.log(isSubString(0,'abc','abc'))
console.log(isSubString(0,'abc','sabc'))
