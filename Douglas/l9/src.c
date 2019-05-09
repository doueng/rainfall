
class N
{
public:
    N(int);
    void setAnnotation(char *param);
private:
    char s[0x6c];
};

/* N::N(int) */

N::N(int param_1)
{
   *this = 0x8048848;
   *(int *)(this + 0x68) = param_1;
   return;
}

/* N::setAnnotation(char*) */

void N::setAnnotation(char *param_1)
{
  size_t __n;

  __n = strlen(param_1);
  memcpy(this + 4,param_1,__n);
  return;
}

void main(int argc,char **argv)
{
  N *this;
  code **this_00;

  if (argc < 2) {
    _exit(1);
  }
  N *n = new N(5);
  /*this = (N *)operator.new(0x6c); // malloc*/
  /*N(5); // initialize*/
  // x $eax
  //   0x804eb70:      0x08048848
  // x $eax+0x68
  //   0x804ebd8:      0x00000005
  /*this_00 = (code **)operator.new(0x6c); //malloc*/
  N((N *)this_00,6); //initialize
  // x $eax
  //   0x804ebe0:      0x08048848
  // x $eax+0x68
  //   0x804ec48:      0x00000006
  setAnnotation(this,argv[1]);
  (**(code **)*this_00)(this_00,this);
  return;
}
