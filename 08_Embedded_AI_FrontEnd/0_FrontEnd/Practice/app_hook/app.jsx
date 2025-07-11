// App.jsx
import React, { useState, useEffect, useRef, useContext, useMemo, useCallback, useReducer, useLayoutEffect, useId, useTransition, useDeferredValue, createContext } from 'react';
import Button from './components/Button';
import Counter from './components/Counter';
import Timer from './components/Timer';
import FocusInput from './components/FocusInput';
import WelcomeUser from './components/WelcomeUser';
import ExpensiveCalc from './components/ExpensiveCalc';
import CallbackExample from './components/CallbackExample';
import ReducerExample from './components/ReducerExample';
import LayoutEffectExample from './components/LayoutEffectExample';
import WindowWidthComponent from './components/WindowWidthComponent';
import ToggleComponent from './components/ToggleComponent';
import EmitCustomEvent from './components/EmitCustomEvent';
import AdvancedHooks from './components/AdvancedHooks';

export const UserContext = createContext();

function App() {
  const [input, setInput] = useState('React');
  const handleInputChange = (e) => setInput(e.target.value);

  return (
    <UserContext.Provider value="Ahmed">
      <div className="p-6 space-y-6">
        <h1 className="text-2xl font-bold">React Hooks, Events, Props & Components Demo</h1>

        <Button label="Simple Button" onClick={() => alert("Button clicked!")} />
        <Counter />
        <Timer />
        <FocusInput />
        <WelcomeUser />
        <ExpensiveCalc input={10} />
        <CallbackExample a={1} b={2} />
        <ReducerExample />
        <LayoutEffectExample />
        <WindowWidthComponent />
        <ToggleComponent />
        <EmitCustomEvent />

        <div>
          <label className="block mb-2">Deferred Input (React 18+):</label>
          <input
            className="border p-2"
            value={input}
            onChange={handleInputChange}
          />
          <AdvancedHooks input={input} />
        </div>
      </div>
    </UserContext.Provider>
  );
}

export default App;

