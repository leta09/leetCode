var createCounter = function(init) {
    curr = init
   return {
       increment: () => {
           ++curr
           return curr
       },
       decrement: () =>{
           --curr
           return curr
       },
       reset: () =>{
           curr = init
           return curr
       },
      
   }
};