USE [CrmEuro]
GO
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE VIEW [dbo].[RcargaView]
as
    SELECT T0.id, T0.numero, T0.fecha, t4.name as 'division', T3.ruta, T2.estatus, T1.chofer, T1.ayudante, T5.placa
    FROM rcarga T0
        LEFT OUTER JOIN rcarga_despacho T1 ON T0.id=T1.rcarga_id
        INNER JOIN rcarga_estatus T2 ON T0.estatus_id=T2.id
        INNER JOIN rcarga_ruta T3 ON T0.ruta_id=T3.id
        INNER JOIN division T4 ON T0.division_id=T4.id
        LEFT OUTER JOIN flota T5 ON T1.vehiculo=T5.id
GO


