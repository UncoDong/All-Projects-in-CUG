package com.test;

import java.util.Enumeration;
import java.util.Iterator;
import java.util.Vector;

public class ConcreteSubject implements Subject {

	private Vector<Observer> observersVector = new Vector<Observer>();
	
	@Override
	public void attcah(Observer observer) {
		// 添加观察者
		observersVector.addElement(observer);
	}

	@Override
	public void detach(Observer observer) {
		// 删除观察者
		observersVector.removeElement(observer);
	}

	@Override
	public void notifyObservers(String s) {
		// 唤醒全部观察者
		
		Iterator<Observer> iterator = observersVector.iterator();
		while (iterator.hasNext()) {
			iterator.next().update(s);
            //System.out.println(iterator.next());
        }

	}

}
