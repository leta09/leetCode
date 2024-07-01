var expect = function(val) {
    const res = {
        toBe: (val2) => {
            if(val === val2){
                return true
            }else{
                throw new Error("Not Equal");
            }
        },
        notToBe: (val2) => {
            if(val !== val2){
                return true
            }else{
                throw new Error("Equal");
            }
        },
    }
    return res
};