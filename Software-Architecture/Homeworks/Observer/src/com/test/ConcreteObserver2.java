package com.test;

public class ConcreteObserver2 implements Observer {

	@Override
	public void update(String s) {
		System.out.println(this.getClass());

	}

}
