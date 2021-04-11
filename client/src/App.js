import React,{useState} from 'react';
import styles from './App.module.css';
import axios from 'axios';

function App() {

  const [state,setState]=useState({
       text:'',
       loading:false,
       next_words:['contemporary','hell','helo','what','why'],
       stage:'completed'
  });

  const corrwrdhandler=()=>{
    let curr_text=state.text;

    setState(prevState=>({...prevState,loading:true}));
    axios.post('/output',{
          text:curr_text,
          type:'correct'
    }).then(res=>{
      const data=res.data.map(el=>el[1]);
      console.log(data);
      setState(prevState=>({...prevState,next_words:data,loading:false,stage:'completed'}));
    }).catch(err=>{
      console.log(err);
      setState(prevState=>({...prevState,loading:false,stage:'completed'}));
    });
    // console.log(curr_text);
  }


  const textchangehandler=async (e)=>{

    let curr_text=e.target.value;
    let typ='complete';

    if(curr_text.charAt(curr_text.length-1)===' ')
    {
      typ='predict';
    }
    
    if(typ==='predict'&&state.stage==='complete'){
      setState(prevState=>({...prevState,text:curr_text}));
      return 0;
    }

    setState(prevState=>({...prevState,loading:true,text:curr_text}));
    try{
      const res = await axios.post('/output',{
            text:curr_text,
            type:typ
            });
      console.log(typ);
      const data=res.data.map(el=>el[1]);
      console.log(data);
      if(typ==='complete')
      setState(prevState=>({...prevState,next_words:data,loading:false,stage:'complete'}));
      else
      setState(prevState=>({...prevState,next_words:data,loading:false,stage:'predict'}));
    }
    catch(err){
      console.log(err);
      setState(prevState=>({...prevState,loading:false}));
    }

  }

  const clickhandler=(el)=>{
      let curr_text=state.text.split(' ');

      curr_text=curr_text.filter(el=>el);
      if(curr_text[curr_text.length-1]===''){
        curr_text.push(el);
      }
      else
      curr_text[curr_text.length-1]=el;
      
      console.log(curr_text);

      setState(prevState=>({...prevState,text:curr_text.join(' '),stage:'completed'}));

  }

  const word_divs=state.next_words.map((el,id)=>{
    return (  <div key={id+'word'} className={styles.words} onClick={()=>clickhandler(el)} value={el}>
                  {el}
              </div>
            );
  }).slice(0,5);




  return (
    <div className={styles.wrapper}>
      <h1>TEXT AUTOCOMPLETION</h1>
      <p>Enter the text in the provided area below <br/>
       the words will be predicted automatically, additionaly <br/>
        the current word can be corrected by clicking on "Correct word" Button provided
      </p>
      <div className={styles.inputwrapper}>
        <label>
        Type sentences here:
        <input type="text" onChange={textchangehandler} value={state.text}></input>
        </label>
        <button onClick={corrwrdhandler}>Correct ME!!</button>
      </div>
      {state.loading
              ?<div className={styles.loader}>Loading...</div>
              :<div className={styles.wordwrapper}>
                  {word_divs}
              </div>
      }
    </div>
  );
}

export default App;
