{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {},
   "outputs": [],
   "source": [
    "class Polygon:\n",
    "    \n",
    "    def __init__(self, edges, radius):\n",
    "        \n",
    "        self._edges = None\n",
    "        self._radius = None\n",
    "        \n",
    "        self.edges = edges\n",
    "        self.radius = radius\n",
    "        \n",
    "    @property\n",
    "    def edges(self):\n",
    "        return self._edges\n",
    "    \n",
    "    @edges.setter\n",
    "    def edges(self, value):\n",
    "        if not isinstance(value, int):\n",
    "            raise TypeError('Number of edges should only be integers')\n",
    "        elif value < 3 :\n",
    "            raise ValueError('There must be atleast 3 edges')\n",
    "        else:\n",
    "            self._edges = value\n",
    "            \n",
    "    @property\n",
    "    def radius(self):\n",
    "        return self._radius\n",
    "    \n",
    "    @radius.setter\n",
    "    def radius(self, value):\n",
    "        if value <= 0 :\n",
    "            raise ValueError('Circumradius can only be positive')\n",
    "        else:\n",
    "            self._radius = value\n",
    "            \n",
    "    def __repr__(self):\n",
    "        return f'{self.__class__.__name__}(edges={self.edges}, radius={self.radius})'"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "metadata": {},
   "outputs": [],
   "source": [
    "p1 = Polygon(3,3)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "Polygon(edges=3, radius=3)"
      ]
     },
     "execution_count": 6,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "p1"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "metadata": {},
   "outputs": [],
   "source": [
    "p2 = Polygon(3, 10)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "Polygon(edges=3, radius=10)"
      ]
     },
     "execution_count": 8,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "p2"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "metadata": {},
   "outputs": [],
   "source": [
    "p1.edges = 5"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "Polygon(edges=5, radius=3)"
      ]
     },
     "execution_count": 11,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "p1"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "metadata": {},
   "outputs": [
    {
     "ename": "TypeError",
     "evalue": "Number of edges should only be integers",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mTypeError\u001b[0m                                 Traceback (most recent call last)",
      "\u001b[1;32m<ipython-input-15-21c79d85008f>\u001b[0m in \u001b[0;36m<module>\u001b[1;34m\u001b[0m\n\u001b[1;32m----> 1\u001b[1;33m \u001b[0mp3\u001b[0m \u001b[1;33m=\u001b[0m \u001b[0mPolygon\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;36m.3\u001b[0m\u001b[1;33m,\u001b[0m\u001b[1;36m0\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m",
      "\u001b[1;32m<ipython-input-4-9e62dc58517f>\u001b[0m in \u001b[0;36m__init__\u001b[1;34m(self, edges, radius)\u001b[0m\n\u001b[0;32m      6\u001b[0m         \u001b[0mself\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0m_radius\u001b[0m \u001b[1;33m=\u001b[0m \u001b[1;32mNone\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m      7\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m----> 8\u001b[1;33m         \u001b[0mself\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0medges\u001b[0m \u001b[1;33m=\u001b[0m \u001b[0medges\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m      9\u001b[0m         \u001b[0mself\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mradius\u001b[0m \u001b[1;33m=\u001b[0m \u001b[0mradius\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m     10\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;32m<ipython-input-4-9e62dc58517f>\u001b[0m in \u001b[0;36medges\u001b[1;34m(self, value)\u001b[0m\n\u001b[0;32m     16\u001b[0m     \u001b[1;32mdef\u001b[0m \u001b[0medges\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mself\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mvalue\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m     17\u001b[0m         \u001b[1;32mif\u001b[0m \u001b[1;32mnot\u001b[0m \u001b[0misinstance\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mvalue\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mint\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m---> 18\u001b[1;33m             \u001b[1;32mraise\u001b[0m \u001b[0mTypeError\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;34m'Number of edges should only be integers'\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m     19\u001b[0m         \u001b[1;32melif\u001b[0m \u001b[0mvalue\u001b[0m \u001b[1;33m<\u001b[0m \u001b[1;36m3\u001b[0m \u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m     20\u001b[0m             \u001b[1;32mraise\u001b[0m \u001b[0mValueError\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;34m'There must be atleast 3 edges'\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;31mTypeError\u001b[0m: Number of edges should only be integers"
     ]
    }
   ],
   "source": [
    "p3 = Polygon(.3,0)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "metadata": {},
   "outputs": [],
   "source": [
    "class Polygon:\n",
    "    \n",
    "    def __init__(self, edges, radius):\n",
    "        \n",
    "        self._edges = None\n",
    "        self._radius = None\n",
    "        \n",
    "        self.edges = edges\n",
    "        self.radius = radius\n",
    "        \n",
    "    @property\n",
    "    def edges(self):\n",
    "        return self._edges\n",
    "    \n",
    "    @edges.setter\n",
    "    def edges(self, value):\n",
    "        if not isinstance(value, int):\n",
    "            raise TypeError('Number of edges should only be integers')\n",
    "        elif value < 3 :\n",
    "            raise ValueError('There must be atleast 3 edges')\n",
    "        else:\n",
    "            self._edges = value\n",
    "            \n",
    "    @property\n",
    "    def radius(self):\n",
    "        return self._radius\n",
    "    \n",
    "    @radius.setter\n",
    "    def radius(self, value):\n",
    "        if value <= 0 :\n",
    "            raise ValueError('Circumradius can only be positive')\n",
    "        else:\n",
    "            self._radius = value\n",
    "            \n",
    "    @property\n",
    "    def vertices(self):\n",
    "        return self.edges\n",
    "            \n",
    "    def __repr__(self):\n",
    "        return f'{self.__class__.__name__}(edges={self.edges}, radius={self.radius})'"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "metadata": {},
   "outputs": [],
   "source": [
    "p1 = Polygon(3,1)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "3"
      ]
     },
     "execution_count": 10,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "p1.vertices"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "1"
      ]
     },
     "execution_count": 11,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "p1.radius"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "metadata": {},
   "outputs": [],
   "source": [
    "p1.edges = 10"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "Polygon(edges=10, radius=1)"
      ]
     },
     "execution_count": 13,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "p1"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "metadata": {},
   "outputs": [
    {
     "ename": "TypeError",
     "evalue": "Number of edges should only be integers",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mTypeError\u001b[0m                                 Traceback (most recent call last)",
      "\u001b[1;32m<ipython-input-15-3f8e57f96f54>\u001b[0m in \u001b[0;36m<module>\u001b[1;34m\u001b[0m\n\u001b[1;32m----> 1\u001b[1;33m \u001b[0mp2\u001b[0m \u001b[1;33m=\u001b[0m \u001b[0mPolygon\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;36m0.1\u001b[0m\u001b[1;33m,\u001b[0m\u001b[1;36m0\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m",
      "\u001b[1;32m<ipython-input-6-0038aed41bf6>\u001b[0m in \u001b[0;36m__init__\u001b[1;34m(self, edges, radius)\u001b[0m\n\u001b[0;32m      6\u001b[0m         \u001b[0mself\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0m_radius\u001b[0m \u001b[1;33m=\u001b[0m \u001b[1;32mNone\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m      7\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m----> 8\u001b[1;33m         \u001b[0mself\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0medges\u001b[0m \u001b[1;33m=\u001b[0m \u001b[0medges\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m      9\u001b[0m         \u001b[0mself\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mradius\u001b[0m \u001b[1;33m=\u001b[0m \u001b[0mradius\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m     10\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;32m<ipython-input-6-0038aed41bf6>\u001b[0m in \u001b[0;36medges\u001b[1;34m(self, value)\u001b[0m\n\u001b[0;32m     16\u001b[0m     \u001b[1;32mdef\u001b[0m \u001b[0medges\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mself\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mvalue\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m     17\u001b[0m         \u001b[1;32mif\u001b[0m \u001b[1;32mnot\u001b[0m \u001b[0misinstance\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mvalue\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mint\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m---> 18\u001b[1;33m             \u001b[1;32mraise\u001b[0m \u001b[0mTypeError\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;34m'Number of edges should only be integers'\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m     19\u001b[0m         \u001b[1;32melif\u001b[0m \u001b[0mvalue\u001b[0m \u001b[1;33m<\u001b[0m \u001b[1;36m3\u001b[0m \u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m     20\u001b[0m             \u001b[1;32mraise\u001b[0m \u001b[0mValueError\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;34m'There must be atleast 3 edges'\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;31mTypeError\u001b[0m: Number of edges should only be integers"
     ]
    }
   ],
   "source": [
    "p2 = Polygon(0.1,0)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 31,
   "metadata": {},
   "outputs": [],
   "source": [
    "import math\n",
    "class Polygon:\n",
    "    \n",
    "    def __init__(self, edges, radius):\n",
    "        \n",
    "        self._edges = None\n",
    "        self._radius = None\n",
    "        \n",
    "        self.edges = edges\n",
    "        self.radius = radius\n",
    "        \n",
    "    @property\n",
    "    def edges(self):\n",
    "        return self._edges\n",
    "    \n",
    "    @edges.setter\n",
    "    def edges(self, value):\n",
    "        if not isinstance(value, int):\n",
    "            raise TypeError('Number of edges should only be integers')\n",
    "        elif value < 3 :\n",
    "            raise ValueError('There must be atleast 3 edges')\n",
    "        else:\n",
    "            self._edges = value\n",
    "            \n",
    "    @property\n",
    "    def radius(self):\n",
    "        return self._radius\n",
    "    \n",
    "    @radius.setter\n",
    "    def radius(self, value):\n",
    "        if value <= 0 :\n",
    "            raise ValueError('Circumradius can only be positive')\n",
    "        else:\n",
    "            self._radius = value\n",
    "            \n",
    "    @property\n",
    "    def vertices(self):\n",
    "        return self.edges\n",
    "    \n",
    "    def interior_angle(self):\n",
    "        return (self.edges - 2) * (180/self.edges)\n",
    "    \n",
    "    def edge_length(self):\n",
    "        return (2 * self.radius) * (math.sin(math.pi/self.edges))\n",
    "    \n",
    "    def area(self):\n",
    "        a = self.radius * math.cos(math.pi / self.edges)\n",
    "        s = self.edge_length()\n",
    "        return (self.edges * s * a) / 2\n",
    "    \n",
    "    def perimeter(self):\n",
    "        s = self.edge_length()\n",
    "        return self.edges * s\n",
    "            \n",
    "    def __repr__(self):\n",
    "        return f'{self.__class__.__name__}(edges={self.edges}, radius={self.radius})'"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 32,
   "metadata": {},
   "outputs": [],
   "source": [
    "p1 = Polygon(3,11.55)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 33,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "60.0"
      ]
     },
     "execution_count": 33,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "p1.interior_angle()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 34,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "20.005186827420534"
      ]
     },
     "execution_count": 34,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "p1.edge_length()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 35,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "173.29493089253043"
      ]
     },
     "execution_count": 35,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "p1.area()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 36,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "60.015560482261606"
      ]
     },
     "execution_count": 36,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "p1.perimeter()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 37,
   "metadata": {},
   "outputs": [],
   "source": [
    "# All imports go here\n",
    "import math\n",
    "\n",
    "# This is a simple Polygon class which creates a polygon \n",
    "# based on the number of edges and the circumradius\n",
    "class Polygon:\n",
    "    \n",
    "    # Initialisation starts here\n",
    "    def __init__(self, edges, radius):\n",
    "        \n",
    "        self._edges = None\n",
    "        self._radius = None\n",
    "        \n",
    "        self.edges = edges\n",
    "        self.radius = radius\n",
    "        \n",
    "    # Getters and setters start here\n",
    "    # edges getter and setter\n",
    "    @property\n",
    "    def edges(self):\n",
    "        return self._edges\n",
    "    \n",
    "    @edges.setter\n",
    "    def edges(self, value):\n",
    "        if not isinstance(value, int):\n",
    "            raise TypeError('Number of edges should only be integers')\n",
    "        elif value < 3 :\n",
    "            raise ValueError('There must be atleast 3 edges')\n",
    "        else:\n",
    "            self._edges = value\n",
    "    \n",
    "    # radius getter and setter        \n",
    "    @property\n",
    "    def radius(self):\n",
    "        return self._radius\n",
    "    \n",
    "    @radius.setter\n",
    "    def radius(self, value):\n",
    "        if value <= 0 :\n",
    "            raise ValueError('Circumradius can only be positive')\n",
    "        else:\n",
    "            self._radius = value\n",
    "            \n",
    "    @property\n",
    "    def vertices(self):\n",
    "        return self.edges\n",
    "    \n",
    "    # Calculates the interior angle of the polygon\n",
    "    def interior_angle(self):\n",
    "        return (self.edges - 2) * (180/self.edges)\n",
    "    \n",
    "    # Calculates the edge length\n",
    "    # All sides have the same length\n",
    "    def edge_length(self):\n",
    "        return (2 * self.radius) * (math.sin(math.pi/self.edges))\n",
    "    \n",
    "    # Calculates area of the polygon\n",
    "    def area(self):\n",
    "        a = self.radius * math.cos(math.pi / self.edges)\n",
    "        s = self.edge_length()\n",
    "        return (self.edges * s * a) / 2\n",
    "    \n",
    "    # Calculates perimeter of the polygon\n",
    "    def perimeter(self):\n",
    "        s = self.edge_length()\n",
    "        return self.edges * s\n",
    "            \n",
    "    def __repr__(self):\n",
    "        return f'{self.__class__.__name__}(edges={self.edges}, radius={self.radius})'"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [],
   "source": [
    "# All imports go here\n",
    "import math\n",
    "\n",
    "# This is a simple Polygon class which creates a polygon \n",
    "# based on the number of edges and the circumradius\n",
    "class Polygon:\n",
    "    \n",
    "    # Initialisation starts here\n",
    "    def __init__(self, edges, radius):\n",
    "        \n",
    "        self._edges = None\n",
    "        self._radius = None\n",
    "        \n",
    "        self.edges = edges\n",
    "        self.radius = radius\n",
    "        \n",
    "    # Getters and setters start here\n",
    "    # edges getter and setter\n",
    "    @property\n",
    "    def edges(self):\n",
    "        return self._edges\n",
    "    \n",
    "    @edges.setter\n",
    "    def edges(self, value):\n",
    "        if not isinstance(value, int):\n",
    "            raise TypeError('Number of edges of a polygon should only be integers')\n",
    "        elif value < 3 :\n",
    "            raise ValueError('There must be atleast 3 edges in a polygon')\n",
    "        else:\n",
    "            self._edges = value\n",
    "    \n",
    "    # radius getter and setter        \n",
    "    @property\n",
    "    def radius(self):\n",
    "        return self._radius\n",
    "    \n",
    "    @radius.setter\n",
    "    def radius(self, value):\n",
    "        if value <= 0 :\n",
    "            raise ValueError('Circumradius can only be positive')\n",
    "        else:\n",
    "            self._radius = value\n",
    "            \n",
    "    @property\n",
    "    def vertices(self):\n",
    "        return self.edges\n",
    "    \n",
    "    # Calculates the interior angle of the polygon\n",
    "    def interior_angle(self):\n",
    "        return (self.edges - 2) * (180/self.edges)\n",
    "    \n",
    "    # Calculates the edge length\n",
    "    # All sides have the same length\n",
    "    def edge_length(self):\n",
    "        return (2 * self.radius) * (math.sin(math.pi/self.edges))\n",
    "    \n",
    "    # Calculates area of the polygon\n",
    "    def area(self):\n",
    "        a = self.radius * math.cos(math.pi / self.edges)\n",
    "        s = self.edge_length()\n",
    "        return (self.edges * s * a) / 2\n",
    "    \n",
    "    # Calculates perimeter of the polygon\n",
    "    def perimeter(self):\n",
    "        s = self.edge_length()\n",
    "        return self.edges * s\n",
    "    \n",
    "    # Equality implementation\n",
    "    # Can compare only Polygons\n",
    "    # Polygons are said to be equal if they have same number of vertices and same circumradius\n",
    "    def __eq__(self, other):\n",
    "        if isinstance(other, Polygon):\n",
    "            return self.edges == other.edges and self.radius == other.radius\n",
    "        else:\n",
    "            raise TypeError('Incompatble type for comparision. Can only compare with another Polygon')\n",
    "            \n",
    "    def __repr__(self):\n",
    "        return f'{self.__class__.__name__}(edges={self.edges}, radius={self.radius})'"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {},
   "outputs": [],
   "source": [
    "p1 = Polygon(3,1)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "metadata": {},
   "outputs": [],
   "source": [
    "p2 = Polygon(3,1)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "True"
      ]
     },
     "execution_count": 6,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "p1 == p2"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "Polygon(edges=3, radius=1)"
      ]
     },
     "execution_count": 7,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "p1"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "Polygon(edges=3, radius=1)"
      ]
     },
     "execution_count": 8,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "p2"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "metadata": {},
   "outputs": [],
   "source": [
    "p1.radius = 10"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "False"
      ]
     },
     "execution_count": 10,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "p1 == p2"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "(Polygon(edges=3, radius=10), Polygon(edges=3, radius=1))"
      ]
     },
     "execution_count": 11,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "p1,p2"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "metadata": {},
   "outputs": [
    {
     "ename": "TypeError",
     "evalue": "Incompatble type for comparision. Can only compare with another Polygon",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mTypeError\u001b[0m                                 Traceback (most recent call last)",
      "\u001b[1;32m<ipython-input-12-754b5931ab26>\u001b[0m in \u001b[0;36m<module>\u001b[1;34m\u001b[0m\n\u001b[1;32m----> 1\u001b[1;33m \u001b[0mp1\u001b[0m \u001b[1;33m==\u001b[0m \u001b[1;36m10\u001b[0m\u001b[1;33m,\u001b[0m\u001b[1;36m3\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m",
      "\u001b[1;32m<ipython-input-1-c4d06002e6ed>\u001b[0m in \u001b[0;36m__eq__\u001b[1;34m(self, other)\u001b[0m\n\u001b[0;32m     73\u001b[0m             \u001b[1;32mreturn\u001b[0m \u001b[0mself\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0medges\u001b[0m \u001b[1;33m==\u001b[0m \u001b[0mother\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0medges\u001b[0m \u001b[1;32mand\u001b[0m \u001b[0mself\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mradius\u001b[0m \u001b[1;33m==\u001b[0m \u001b[0mother\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mradius\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m     74\u001b[0m         \u001b[1;32melse\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m---> 75\u001b[1;33m             \u001b[1;32mraise\u001b[0m \u001b[0mTypeError\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;34m'Incompatble type for comparision. Can only compare with another Polygon'\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m     76\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m     77\u001b[0m     \u001b[1;32mdef\u001b[0m \u001b[0m__repr__\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mself\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;31mTypeError\u001b[0m: Incompatble type for comparision. Can only compare with another Polygon"
     ]
    }
   ],
   "source": [
    "p1 == 10,3"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "metadata": {},
   "outputs": [
    {
     "ename": "TypeError",
     "evalue": "Incompatble type for comparision. Can only compare with another Polygon",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mTypeError\u001b[0m                                 Traceback (most recent call last)",
      "\u001b[1;32m<ipython-input-13-1a5ac8a3d3d7>\u001b[0m in \u001b[0;36m<module>\u001b[1;34m\u001b[0m\n\u001b[1;32m----> 1\u001b[1;33m \u001b[0mp1\u001b[0m \u001b[1;33m==\u001b[0m \u001b[1;36m5\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m",
      "\u001b[1;32m<ipython-input-1-c4d06002e6ed>\u001b[0m in \u001b[0;36m__eq__\u001b[1;34m(self, other)\u001b[0m\n\u001b[0;32m     73\u001b[0m             \u001b[1;32mreturn\u001b[0m \u001b[0mself\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0medges\u001b[0m \u001b[1;33m==\u001b[0m \u001b[0mother\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0medges\u001b[0m \u001b[1;32mand\u001b[0m \u001b[0mself\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mradius\u001b[0m \u001b[1;33m==\u001b[0m \u001b[0mother\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mradius\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m     74\u001b[0m         \u001b[1;32melse\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m---> 75\u001b[1;33m             \u001b[1;32mraise\u001b[0m \u001b[0mTypeError\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;34m'Incompatble type for comparision. Can only compare with another Polygon'\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m     76\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m     77\u001b[0m     \u001b[1;32mdef\u001b[0m \u001b[0m__repr__\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mself\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;31mTypeError\u001b[0m: Incompatble type for comparision. Can only compare with another Polygon"
     ]
    }
   ],
   "source": [
    "p1 == 5"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "True"
      ]
     },
     "execution_count": 14,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "p1 == Polygon(3,10)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "False"
      ]
     },
     "execution_count": 16,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "p1 == Polygon(3,100)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 17,
   "metadata": {},
   "outputs": [],
   "source": [
    "# All imports go here\n",
    "import math\n",
    "\n",
    "# This is a simple Polygon class which creates a polygon \n",
    "# based on the number of edges and the circumradius\n",
    "class Polygon:\n",
    "    \n",
    "    # Initialisation starts here\n",
    "    def __init__(self, edges, radius):\n",
    "        \n",
    "        self._edges = None\n",
    "        self._radius = None\n",
    "        \n",
    "        self.edges = edges\n",
    "        self.radius = radius\n",
    "        \n",
    "    # Getters and setters start here\n",
    "    # edges getter and setter\n",
    "    @property\n",
    "    def edges(self):\n",
    "        return self._edges\n",
    "    \n",
    "    @edges.setter\n",
    "    def edges(self, value):\n",
    "        if not isinstance(value, int):\n",
    "            raise TypeError('Number of edges of a polygon should only be integers')\n",
    "        elif value < 3 :\n",
    "            raise ValueError('There must be atleast 3 edges in a polygon')\n",
    "        else:\n",
    "            self._edges = value\n",
    "    \n",
    "    # radius getter and setter        \n",
    "    @property\n",
    "    def radius(self):\n",
    "        return self._radius\n",
    "    \n",
    "    @radius.setter\n",
    "    def radius(self, value):\n",
    "        if value <= 0 :\n",
    "            raise ValueError('Circumradius of a polygon can only be positive')\n",
    "        else:\n",
    "            self._radius = value\n",
    "            \n",
    "    @property\n",
    "    def vertices(self):\n",
    "        return self.edges\n",
    "    \n",
    "    # Calculates the interior angle of the polygon\n",
    "    def interior_angle(self):\n",
    "        return (self.edges - 2) * (180/self.edges)\n",
    "    \n",
    "    # Calculates the edge length\n",
    "    # All sides have the same length\n",
    "    def edge_length(self):\n",
    "        return (2 * self.radius) * (math.sin(math.pi/self.edges))\n",
    "    \n",
    "    # Calculates area of the polygon\n",
    "    def area(self):\n",
    "        a = self.radius * math.cos(math.pi / self.edges)\n",
    "        s = self.edge_length()\n",
    "        return (self.edges * s * a) / 2\n",
    "    \n",
    "    # Calculates perimeter of the polygon\n",
    "    def perimeter(self):\n",
    "        s = self.edge_length()\n",
    "        return self.edges * s\n",
    "    \n",
    "    # Equality implementation\n",
    "    # Can compare only Polygons\n",
    "    # Polygons are said to be equal if they have same number of vertices and same circumradius\n",
    "    def __eq__(self, other):\n",
    "        if isinstance(other, Polygon):\n",
    "            return self.edges == other.edges and self.radius == other.radius\n",
    "        else:\n",
    "            raise TypeError('Incompatble type for comparision. Can only compare with another Polygon')\n",
    "            \n",
    "    # '>' operator implementation\n",
    "    # Polygons are compared based on the number of vertices\n",
    "    def __gt__(self, other):\n",
    "        if isinstance(other, Polygon):\n",
    "            return self.edges > other.edges\n",
    "        else:\n",
    "            raise TypeError('Incompatble type for comparision. Can only compare with another Polygon')\n",
    "            \n",
    "    # Representation of Polygon object\n",
    "    def __repr__(self):\n",
    "        return f'{self.__class__.__name__}(edges={self.edges}, radius={self.radius})'"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 18,
   "metadata": {},
   "outputs": [],
   "source": [
    "p1 = Polygon(3,10)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 19,
   "metadata": {},
   "outputs": [],
   "source": [
    "p2 = Polygon(4,1)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 20,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "False"
      ]
     },
     "execution_count": 20,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "p1 > p2"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 21,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "True"
      ]
     },
     "execution_count": 21,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "p2 > p1"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 22,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "True"
      ]
     },
     "execution_count": 22,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "p1 < p2"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 23,
   "metadata": {},
   "outputs": [
    {
     "ename": "TypeError",
     "evalue": "'<=' not supported between instances of 'Polygon' and 'Polygon'",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mTypeError\u001b[0m                                 Traceback (most recent call last)",
      "\u001b[1;32m<ipython-input-23-f5a47ee2adaf>\u001b[0m in \u001b[0;36m<module>\u001b[1;34m\u001b[0m\n\u001b[1;32m----> 1\u001b[1;33m \u001b[0mp1\u001b[0m \u001b[1;33m<=\u001b[0m \u001b[0mp2\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m",
      "\u001b[1;31mTypeError\u001b[0m: '<=' not supported between instances of 'Polygon' and 'Polygon'"
     ]
    }
   ],
   "source": [
    "p1 <= p2"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.8.3"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
