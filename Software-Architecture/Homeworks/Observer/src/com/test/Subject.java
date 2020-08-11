package com.test;

public interface Subject {
	public void attcah(Observer observer);
	public void detach(Observer observer);
	void notifyObservers(String s);
}
