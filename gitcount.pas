program GitFileCount;

uses
  Process, SysUtils, Classes;

var
  AProcess: TProcess;
  OutputString: TStringList;
begin
  AProcess := TProcess.Create(nil);
  OutputString := TStringList.Create;

  AProcess.Executable := 'git';
  AProcess.Parameters.Add('ls-files');
  AProcess.Options := [poUsePipes, poWaitOnExit];
  AProcess.Execute;

  OutputString.LoadFromStream(AProcess.Output);
  Writeln(OutputString.Count);

  AProcess.Free;
  OutputString.Free;
end.