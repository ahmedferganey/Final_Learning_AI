import React, { createContext, useEffect, useState } from "react";
import { auth } from "../utils/firebase";
import {
  signInWithEmailAndPassword,
  createUserWithEmailAndPassword, // ✅ ADD THIS
  onAuthStateChanged,
  signOut,
} from "firebase/auth";

// Create Context
export const AuthContext = createContext();

// Provider Component
export const AuthProvider = ({ children }) => {
  const [user, setUser] = useState(null);
  const [loading, setLoading] = useState(true);

  // Listen to auth state changes
  useEffect(() => {
    const unsubscribe = onAuthStateChanged(auth, (firebaseUser) => {
      setUser(firebaseUser);
      setLoading(false);
    });
    return () => unsubscribe();
  }, []);

  // ✅ Login handler
  const login = (email, password) => {
    return signInWithEmailAndPassword(auth, email, password)
      .then(() => ({ success: true }))
      .catch((err) => ({
        success: false,
        message: err.message || "Login failed",
      }));
  };

  // ✅ Signup handler
  const signup = (email, password) => {
    return createUserWithEmailAndPassword(auth, email, password)
      .then(() => ({ success: true }))
      .catch((err) => ({
        success: false,
        message: err.message || "Signup failed",
      }));
  };

  // ✅ Logout handler
  const logout = () => signOut(auth);

  return (
    <AuthContext.Provider value={{ user, login, signup, logout, loading }}>
      {children}
    </AuthContext.Provider>
  );
};

export default AuthContext;

