const assert=require('node:assert/strict');
const {run}=require('./docs/demo.js');
const a=run({mode:'original'}),b=run({mode:'edges'});assert.equal(a.image[32][32],220);assert.equal(b.image[32][32],0);assert.ok(b.image[32][17]>0);assert.throws(()=>run({mode:'invalid'}));
console.log('Browser demo behavior checks passed');
